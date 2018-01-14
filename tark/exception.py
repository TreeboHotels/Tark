

class InvalidActionClass(BaseException):

    def __init__(self, action_class):
        """
        raised when an invalid action class is added

        :param action_class: the action class
        """
        self.action_class = action_class

        message = "Invalid Action class given {}".format(self.action_class)

        super(InvalidActionClass, self).__init__(message)


class InvalidRuleVariableTypeClass(BaseException):

    def __init__(self, rule_variable_type):
        """
        raised when an invalid rule variable type class is added

        :param action_class: the rule variable type class
        """
        self.rule_variable_type = rule_variable_type

        message = "Invalid Rule variable type class given {}".format(self.rule_variable_type)

        super(InvalidRuleVariableTypeClass, self).__init__(message)


class ConflictingPolicies(BaseException):

    def __init__(self, policies, filters, domain):
        """
        raised when an invalid action class is added

        :param action_class: the action class
        """
        self.policy_names = [p.name for p in policies]
        self.filters = filters
        self.domain = domain

        message = "Conflicting policies {} found for domain {} and filters {}".format(self.policy_names,
                                                                                      self.domain,
                                                                                      self.filters)

        super(InvalidActionClass, self).__init__(message)
