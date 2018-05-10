import logging


from tark import constants
from tark.entities.models import policy_group
from tark.engine import conflict_resolvers
from tark.exception import ConflictingPolicies

logger = logging.getLogger(constants.TARK_LOGGER_PREFIX + __name__)


class PolicyEngine(object):

    @classmethod
    def filter_policy_groups(cls, filters, domain):
        """
        Get all the matching policy groups for given domain and filters
        :param domain: 
        :param filters: 
        :return: 
        """
        if not domain:
            raise KeyError("Domain cannot be None")

        matched_policy_group_list = []
        logger.debug("Got policy group matching for domain: {} and filters: {}".format(domain, filters))
        domain_policy_groups = policy_group.PolicyGroup.select().where(policy_group.PolicyGroup.domain == domain)

        for policy_group_obj in domain_policy_groups:
            if policy_group_obj.match(filters):
                matched_policy_group_list.append(policy_group_obj)
                logger.debug("Policy Group: {} matched for filters: {}".format(policy_group_obj.name, filters))

        logger.info("Policy groups matching filters: {} are {}."
                    .format(filters, [p.name for p in matched_policy_group_list]))

        return matched_policy_group_list

    @classmethod
    def match(cls, filters, domain=policy_group.PolicyGroup.DEFAULT_DOMAIN, match_only_one=True):

        matched_policies = []
        # first get policy groups
        logger.debug("Got policy matching for domain: {} and filters: {}".format(domain, filters))

        filtered_policy_groups = cls.filter_policy_groups(filters, domain)

        if len(filtered_policy_groups) <= 0:
            logger.error("No policy group found for for filter: {}".format(filters))
            return None

        for pg in filtered_policy_groups:
            for policy_obj in pg.policies:
                if policy_obj.match(filters):
                    matched_policies.append(policy_obj)
                    logger.debug("Got policy matching for Policy: {} filters: {}".format(policy_obj.name, filters))

        if not matched_policies or len(matched_policies) == 0:
            logger.error("No Policy for for filter: {}".format(filters))
            return None

        if not match_only_one:
            logger.debug("Got policy matching for domain: {} and filters: {}".format(domain, filters))
            return matched_policies

        if len(matched_policies) > 1:
            matched_policies = conflict_resolvers.ConflictResolvers.resolve(matched_policies)

        if len(matched_policies) > 1:
            logger.error("Conflicting Policies {} for filter: {}".format(matched_policies, filters))
            raise ConflictingPolicies(matched_policies, filters, domain)

        return matched_policies[0]

    @classmethod
    def match_policy_and_act(cls, filters, domain=policy_group.PolicyGroup.DEFAULT_DOMAIN):
        """
        Match the policy based on the supplied filters and runs the action associated with it
        :param domain: The domain of the policy
        :param filters: the set of filters to be used by policy engine to filter the policy
        :return: the return value of the action to be run
        """

        policy = cls.match(filters, domain)

        if policy is None:
            return False

        return policy.act(policy.action_parameters, filters)


