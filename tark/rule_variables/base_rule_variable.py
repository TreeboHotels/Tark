from abc import abstractmethod


class BaseRuleVariable(object):

    @abstractmethod
    def get_value(self):
        """
        abstart function to be overridded by all overriding class
        :return: 
        """
        pass
