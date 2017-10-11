from abc import abstractmethod


class BaseOperator(object):
    operator_type = "BASE"

    @abstractmethod
    def operate(self, operand_one, operand_two):
        """
        abstart function to be overridden by all overriding class
        :param operand_one: the LDS operand
        :param operand_two: the THS operand
        :return: A True or false response
        """
        pass