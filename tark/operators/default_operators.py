
from tark.operators.base_operator import BaseOperator


class EqualOperator(BaseOperator):

    operator_type = "EQUAL"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() == operand_two.get_value()


class GreaterThanOperator(BaseOperator):

    operator_type = "GREATER_THAN"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value > operand_two.get_value()


class LessThanOperator(BaseOperator):

    operator_type = "LESS_THAN"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() < operand_two.get_value()


class GreaterThanEqualOperator(BaseOperator):

    operator_type = "GREATER_THAN_EQUAL"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() >= operand_two.get_value()


class LessThanEqualOperator(BaseOperator):

    operator_type = "LESS_THAN_EQUAL"

    def operate(self, operand_one, operand_two):
        return operand_one.get_value() <= operand_two.get_value()