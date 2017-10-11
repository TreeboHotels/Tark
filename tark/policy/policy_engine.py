import logging
import json

from tark import constants
from tark import utils
from tark.policy.policy_manager import PolicyManager
from tark.actions.action_manager import ActionManager
from tark.constants import PolicyQueryStatus, ActionTypes

logger = logging.getLogger(constants.TARK_LOGGER_PREFIX + __name__)


class PolicyEngine(object):

    @classmethod
    def match_policy_and_act(cls, domain, filters):
        """
        Match the policy based on the supplied filters and runs the action associated with it
        :param domain: The domain of the policy
        :param filters: the set of filters to be used by policy engine to filter the policy
        :return: the return value of the action to be run
        """

        policy_manager = PolicyManager()

        policies = policy_manager.get_matching_policies(domain, filters)

        if len(policies) == 0:
            return PolicyQueryStatus.NO_MATCHING_POLICY, None

        selected_policies = policy_manager.get_policy_with_action(policies, ActionTypes.VALUE_CALCULATOR)

        if not selected_policies or len(selected_policies) == 0:
            logger.error("No Policy for action {}: for filter: {}".format(ActionTypes.VALUE_CALCULATOR,
                                                                          filters))
            return PolicyQueryStatus.NO_MATCHING_POLICY, None

        if len(selected_policies) > 1:
            logger.error("Conflicting Policy for action {}: for filter: {}".format(ActionTypes.VALUE_CALCULATOR,
                                                                                   filters))
            return PolicyQueryStatus.CONFLICTING_POLICY, None

        policy = selected_policies[0]

        action = ActionManager.get_action_handler(policy.action)

        filter_parameters = utils.get_filtered_keys(policy.action.key_list, filters)

        argument_list = utils.get_filtered_keys(policy.action.argument_list, json.loads(policy.action_parameters))

        return_val = action.act(filter_parameters, argument_list)

        return PolicyQueryStatus.QUERY_SUCCESS, return_val