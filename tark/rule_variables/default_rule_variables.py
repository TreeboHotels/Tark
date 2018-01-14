from datetime import datetime

from tark import constants
from tark.rule_variables.base_rule_variable import BaseRuleVariableType


class LabeledInt(BaseRuleVariableType):

    NAME = 'labeled_int'

    def __init__(self, args, variables):
        self.value = int(variables.get(args))

    def get_value(self):
        return self.value


class LabeledFloat(BaseRuleVariableType):

    NAME = 'labeled_float'

    def __init__(self, args, variables):
        self.value = float(variables.get(args))

    def get_value(self):
        return self.value


class LabeledString(BaseRuleVariableType):

    NAME = 'labeled_string'

    def __init__(self, args, variables):
        self.value = str(variables.get(args))

    def get_value(self):
        return self.value


class ConstInt(BaseRuleVariableType):

    NAME = 'const_int'

    def __init__(self, args, variables):
        self.value = int(args)

    def get_value(self):
        return self.value


class ConstFloat(BaseRuleVariableType):

    NAME = 'const_float'

    def __init__(self, args, variables):
        self.value = float(args)

    def get_value(self):
        return self.value


class ConstString(BaseRuleVariableType):

    NAME = 'const_string'

    def __init__(self, args, variables):
        self.value = str(args)

    def get_value(self):
        return self.value


class NoOfDays(BaseRuleVariableType):

    NAME = 'no_of_days'

    def __init__(self, args, variables):

        keys = args.split(",")

        start = keys[0]
        end = keys[1]

        self.start_date = datetime.strptime(variables.get(start), constants.DATETIME_FORMAT_STRING)
        self.end_date = datetime.strptime(variables.get(end), constants.DATETIME_FORMAT_STRING)

        delta = self.end_date - self.start_date
        self.value = delta.days

    def get_value(self):
        return self.value

