from tark.rule_variables import default_rule_variables
from tark import utils
from tark.models.all_models import RuleVariable

class RuleVariableManager(object):

    rule_variables_mapping = {
        "INT": default_rule_variables.IntRuleVariable,
        "STRING": default_rule_variables.StringRuleVariable,
        "FLOAT": default_rule_variables.FloatRuleVariable,
        "NO_OF_DAYS": default_rule_variables.NoOfDaysRuleVariable,
    }

    @classmethod
    def add_rule_variable(cls, **kwargs):
        return RuleVariable.create(**kwargs)

    @classmethod
    def get_rule_variable(cls, rule_variable_obj, value_list):
        """
        return the rule variable for the given type
        :param rule_variable_obj: the type of the rule variable
        :param value_list: the list of values to searched for values to be passed to rule variable
        :return: the rule variable of riven type
        """

        if not rule_variable_obj or not value_list:
            raise KeyError("rule variable obj or value list cannot be none")

        rule_variable_class = cls.rule_variables_mapping.get(rule_variable_obj.type)

        if not rule_variable_class:
            raise KeyError("No rule variable found for given type: {}".format(rule_variable_obj.type))

        filtered_arguments = utils.get_filtered_keys_from_map(rule_variable_obj.argument_list, value_list)

        rule_variable = rule_variable_class(filtered_arguments)

        return rule_variable
