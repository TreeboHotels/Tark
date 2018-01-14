from abc import abstractmethod


class BaseAction(object):

    @abstractmethod
    def act(self, args, filters):
        """
        abstart function to be overridded by all overriding class
        :param args: list of action arguments expected by the action
        :param filters: list of filter arguments expected by the action
        :return: A response which corresponds to the action to be taken
        """
        pass