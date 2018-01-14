from tark.operators import default_operators


class OperatorManager(object):

    comparator_mapping = {
        default_operators.Equal.NAME: default_operators.Equal,
        default_operators.NotEqual.NAME: default_operators.NotEqual,
        default_operators.GreaterThan.NAME: default_operators.GreaterThan,
        default_operators.LessThan.NAME: default_operators.LessThan,
        default_operators.GreaterThanEqual.NAME: default_operators.GreaterThanEqual,
        default_operators.LessThanEqual.NAME: default_operators.LessThanEqual
    }

    logical_operator_mapping = {
        default_operators.And.NAME: default_operators.And,
        default_operators.Or.NAME: default_operators.Or
    }

    @classmethod
    def register_comparator(cls, name, class_def):

        if name is None or class_def is None:
            raise KeyError("name or class_def cannot be None")
        cls.comparator_mapping[name] = class_def

    @classmethod
    def get_comparator(cls, name):
        """
        return the comparator for the given type
        :param name: the type of the comparator
        :return: the operator of given type
        """

        if not name:
            raise KeyError("name cannot be none")

        operator = cls.comparator_mapping.get(name)

        if not operator:
            raise KeyError("No operator found for given name: {}".format(name))

        return operator

    @classmethod
    def get_logic_operator(cls, name):
        """
        return the operator for the given type
        :param name: the type of the operator
        :return: the operator of given type
        """

        if not name:
            raise KeyError("name cannot be none")

        operator = cls.logical_operator_mapping.get(name)

        if not operator:
            raise KeyError("No operator found for given name: {}".format(name))

        return operator
