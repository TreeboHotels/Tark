
from tark.operators.base_operator import BaseOperator


class Equal(BaseOperator):

    NAME = "equal"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() == operand_two.get_value()


class NotEqual(BaseOperator):

    NAME = "not_equal"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() != operand_two.get_value()


class GreaterThan(BaseOperator):

    NAME = "greater_than"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value > operand_two.get_value()


class LessThan(BaseOperator):

    NAME = "less_than"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() < operand_two.get_value()


class GreaterThanEqual(BaseOperator):

    NAME = "greater_than_equal"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() >= operand_two.get_value()


class LessThanEqual(BaseOperator):

    NAME = "less_than_equal"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() <= operand_two.get_value()


class And(BaseOperator):

    NAME = "and"

    def operate(self, operand_one, operand_two):
        return operand_one and operand_two


class Or(BaseOperator):

    NAME = "or"

    def operate(self, operand_one, operand_two):
        return operand_one or operand_two
