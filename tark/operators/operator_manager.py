from tark.operators import default_operators
from tark.models.all_models import Operator


class OperatorManager(object):

    operator_mapping = {
        "EQUAL": default_operators.EqualOperator,
        "LESS_THAN": default_operators.LessThanOperator,
        "GREATER_THAN": default_operators.GreaterThanOperator,
        "LESS_THAN_EQUAL": default_operators.LessThanEqualOperator,
        "GREATER_THAN_EQUAL": default_operators.GreaterThanEqualOperator
    }

    @classmethod
    def add_operator(cls, **kwargs):
        return Operator.create(**kwargs)

    @classmethod
    def get_operator(cls, operator_type):
        """
        return the operator for the given type
        :param operator_type: the type of the operator
        :return: the operator of given type
        """

        if not operator_type:
            raise KeyError("operator_type cannot be none")

        operator = cls.operator_mapping.get(operator_type)

        if not operator:
            raise KeyError("No operator found for given type: {}".format(operator_type))

        return operator
