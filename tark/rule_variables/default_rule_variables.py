from datetime import datetime

from tark import constants
from tark.rule_variables.base_rule_variable import BaseRuleVariable


class IntRuleVariable(BaseRuleVariable):

    def __init__(self, argument_list):
        if not argument_list or not argument_list.get("value"):
            raise KeyError("unable to find key value in argument list: ".format(argument_list))
        self.value = int(argument_list.get("value"))

    def get_value(self):
        return self.value


class FloatRuleVariable(BaseRuleVariable):

    def __init__(self, argument_list):
        if not argument_list or not argument_list.get("value"):
            raise KeyError("unable to find key value in argument list: ".format(argument_list))
        self.value = float(argument_list.get("value"))

    def get_value(self):
        return self.value


class StringRuleVariable(BaseRuleVariable):

    def __init__(self, argument_list):
        if not argument_list or not argument_list.get("value"):
            raise KeyError("unable to find key value in argument list: ".format(argument_list))
        self.value = str(argument_list.get("value"))

    def get_value(self):
        return self.value


class NoOfDaysRuleVariable(BaseRuleVariable):

    def __init__(self, argument_list):
        if not argument_list or not argument_list.get("start_date") or not argument_list.get("end_date"):
            raise KeyError("unable to find key start_date or end_date in argument list: ".format(argument_list))

        self.start_date = datetime.strptime(argument_list.get("start_date"), constants.DATETIME_FORMAT_STRING)
        self.end_date = datetime.strptime(argument_list.get("end_date"), constants.DATETIME_FORMAT_STRING)

        delta = self.end_date - self.start_date
        self.value = delta.days

    def get_value(self):
        return self.value

