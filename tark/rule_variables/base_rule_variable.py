from abc import abstractmethod


class BaseRuleVariableType(object):

    @abstractmethod
    def get_value(self):
        """
        abstart function to be overridded by all overriding class
        :return: 
        """
        pass
