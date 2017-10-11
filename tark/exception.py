

class InvalidActionClass(BaseException):

    def __init__(self, action_class):
        """
        raised when an invalid action class is added

        :param action_class: the action class
        """
        self.action_class = action_class

        message = "Invalid Action class given {}".format(self.action_class)

        super(InvalidActionClass, self).__init__(message)
