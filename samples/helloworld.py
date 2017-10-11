from tark import core
from tark.core import BaseAction
from tark.constants import ActionTypes


class TestAction(BaseAction):
    def act(self, filter_arguments, action_arguments):
        print("got filter_arguments: {} and action_arguments: {}".format(filter_arguments, action_arguments))

        return 99.00


def create_policy():

    tark = core.Tark(config_path='tark.yaml')

    action = core.action.add_action(TestAction,
                                    name="refund_action",
                                    type=ActionTypes.VALUE_CALCULATOR,
                                    domain="refund",
                                    description="this a test refund action",
                                    key_list="pre_tax_price,tax_price",
                                    argument_list="discount"
                                    )
    core.policy.create_policy(name="test_policy_1",
                              domain="refund",
                              description="this a test refund action",
                              action=action,
                              action_parameters="{\"discount\": 40 }"
                              )

create_policy()
