from abc import abstractmethod


class BaseAction(object):

    @abstractmethod
    def act(self, filter_arguments, action_arguments):
        """
        abstart function to be overridded by all overriding class
        :param filter_arguments: list of filter arguments expected by the action
        :param action_arguments: list of action arguments expected by the action
        :return: A response which corresponds to the action to be taken
        """
        pass