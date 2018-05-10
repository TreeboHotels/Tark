from datetime import datetime

from tark import constants
from tark.rule_variables.base_rule_variable import BaseRuleVariableType


class LabeledInt(BaseRuleVariableType):

    NAME = 'labeled_int'

    def __init__(self, args, variables):
        self.label = args.get("label")
        self.value = int(variables.get(self.label))

    def get_value(self):
        return self.value


class LabeledFloat(BaseRuleVariableType):

    NAME = 'labeled_float'

    def __init__(self, args, variables):
        self.label = args.get("label")
        self.value = float(variables.get(self.label))

    def get_value(self):
        return self.value


class LabeledString(BaseRuleVariableType):

    NAME = 'labeled_string'

    def __init__(self, args, variables):
        self.label = args.get("label")
        self.value = str(variables.get(self.label))

    def get_value(self):
        return self.value


class ConstInt(BaseRuleVariableType):

    NAME = 'const_int'

    def __init__(self, args, variables):
        self.value = int(args.get("value"))

    def get_value(self):
        return self.value


class ConstFloat(BaseRuleVariableType):

    NAME = 'const_float'

    def __init__(self, args, variables):
        self.value = float(args.get("value"))

    def get_value(self):
        return self.value


class ConstString(BaseRuleVariableType):

    NAME = 'const_string'

    def __init__(self, args, variables):
        self.value = str(args.get("value"))

    def get_value(self):
        return self.value


class NoOfDays(BaseRuleVariableType):

    NAME = 'no_of_days'

    def __init__(self, args, variables):

        start = args.get("start_date")
        end = args.get("end_date")

        self.start_date = datetime.strptime(variables.get(start), constants.DATETIME_FORMAT_STRING)
        self.end_date = datetime.strptime(variables.get(end), constants.DATETIME_FORMAT_STRING)

        delta = self.end_date - self.start_date
        self.value = delta.days

    def get_value(self):
        return self.value

