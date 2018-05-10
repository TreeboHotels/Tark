from tark import core, constants, ComplexRule, BaseAction


class TestAction(BaseAction):
    def act(self, filter_arguments, action_arguments):
        print("got filter_arguments: {} and action_arguments: {}".format(filter_arguments, action_arguments))

        return 99.00


def create_policy():

    tark = core.Tark(config_path='tark.yaml')

    action_var = tark.actions.register_action(action_class=TestAction,
                                        name="refund_action",
                                        argument_keys='discount',
                                        description="this a test refund action")

    rule_var_11 = tark.rules.create_rule_variable(name="booking_channel",
                                            type=constants.DefaultRuleVariableTypes.LABELED_STRING,
                                            args=dict(label='booking_channel'))

    rule_var_12 = tark.rules.create_rule_variable(name="channel_web",
                                            type=constants.DefaultRuleVariableTypes.CONST_STRING,
                                            args=dict(value='WEB'))
    rule_1 = tark.rules.create_rule(name="is_web_channel",
                              lhs=rule_var_11,
                              comparator=constants.DefaultComparators.EQUAL,
                              rhs=rule_var_12,
                              description="rule to check if channel is web or not")

    rule_var_21 = tark.rules.create_rule_variable(name="booking_rate_plan",
                                            type=constants.DefaultRuleVariableTypes.LABELED_STRING,
                                            args=dict(label='booking_rate_plan'))

    rule_var_22 = tark.rules.create_rule_variable(name="rate_plan_refundable",
                                         type=constants.DefaultRuleVariableTypes.CONST_STRING,
                                            args=dict(value='EP'))
    rule_2 = tark.rules.create_rule(name="is_rate_plan_refundable",
                              lhs=rule_var_21,
                              comparator=constants.DefaultComparators.EQUAL,
                              rhs=rule_var_22,
                              description="rule to check if rate plan is refundable rate plan.")

    # Create rule equation
    complex_rule_1 = ComplexRule(rule_1,
                                 tark.operators.get_logic_operator(constants.DefaultLogicalOperators.AND),
                                 rule_2)

    equation_1 = tark.rules.create_rule_equation(name="is_booking_web_and_refundable",
                                           description="Check is booking is web channel and refundable",
                                           equation=complex_rule_1.dict)

    # Create policy group
    policy_group_var = tark.policies.create_policy_group(name="refund_policies",
                                                  domain="refund",
                                                  description="All the policies related to refund")

    policy_var = tark.policies.create_policy(name="test_policy_1",
                                      description="this a test refund action",
                                      policy_group=policy_group_var,
                                      rule_equation=equation_1,
                                      action=action_var,
                                      action_parameters="{\"discount\": 40 }"
                                      )

    return tark


def test_match():
    tark = core.Tark(config_path='tark.yaml')

    filters = dict(booking_channel="WEB",
                   booking_rate_plan="EP",
                   checkin_date="10-12-2017",
                   checkout_date="12-12-2017")

    matched_policy = tark.engine.match(filters, "refund")

    if matched_policy:
        print(matched_policy.name)
    else:
        print("No policy found")

    return matched_policy

test_match()

