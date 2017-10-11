import logging

from tark import constants
from tark.models.all_models import PolicyGroup, Policy, Rule, PolicyToRulesMap, PolicyGroupToRulesMap
from tark.rule_variables.rule_variable_manager import RuleVariableManager
from tark.operators.operator_manager import OperatorManager


logger = logging.getLogger(constants.TARK_LOGGER_PREFIX + __name__)


class PolicyManager(object):

    @classmethod
    def create_policy(cls, **kwargs):
        # add validation
        Policy.create(**kwargs)

    @classmethod
    def create_policy_group(cls, **kwargs):
        #TODO: Add validation
        PolicyGroup.create(**kwargs)

    @classmethod
    def create_rule(cls, **kwargs):
        # add validation
        Rule.create(**kwargs)

    @classmethod
    def add_rule_to_policy(cls, policy, rule, order):
        # add validation
        PolicyToRulesMap.create(policy=policy, rule=rule, order=order)

    @classmethod
    def add_rule_to_policy_group(cls, policy_group, rule, order):
        # add validation
        PolicyGroupToRulesMap.create(policy_group=policy_group, rule=rule, order=order)

    @classmethod
    def get_matching_policies(cls, domain, filters):
        """
        get the matching matching policies for a given domain and provided filters
        :param domain: Domain of policies like refund policy etc.,
        :param filters: The filters to be use to filter out the policies we are looking for.
        :return: A list of policy objects which match the given filters of the given domain.
        """
        if not domain:
            raise KeyError("Domain cannot be None")

        matched_policy_list = []
        logger.debug("Got policy matching for domain: {} and filters: {}".format(domain, filters))
        domain_policies = Policy.select().where(Policy.domain == domain)

        for policy in domain_policies:
            if cls.does_policy_match(policy, filters):
                logger.debug("Policy: {} matched for filters: {}".format(policy.name, filters))
                matched_policy_list.append(policy)

        logger.info("Policies matching filters: {} are {}.".format(filters, [p.name for p in matched_policy_list]))

        return matched_policy_list

    @classmethod
    def get_policy_with_action(cls, policies, action_type):
        """
        filter the policies based on action type and return 
        :param policies: The list of policies to be filtered
        :param action_type: Type of action to be filtered upon
        :return: list of policies with given action type
        """

        selected_policies = []
        for policy in policies:
            if policy.action.type == action_type:
                selected_policies.append(policy)

        return selected_policies

    @classmethod
    def does_policy_match(cls, policy, filters):
        """
        Does the given policy match the given filters
        :param policy: the policy object to be matched
        :param filters: filters to be matched with
        :return: True is all rules match else false
        """

        is_a_match = True
        for rule_map in PolicyToRulesMap.select().where(PolicyToRulesMap.policy == policy):
            rule = rule_map.rule
            operand_one = RuleVariableManager.get_rule_variable(rule.operand_one,
                                                                filters.update(rule.operand_one_values))
            operand_two = RuleVariableManager.get_rule_variable(rule.operand_two,
                                                                filters.update(rule.operand_two_values))
            operator = OperatorManager.get_operator(rule.comparator.type)
            if not operator.operate(operand_one, operand_two):
                is_a_match = False
                break
        return is_a_match
