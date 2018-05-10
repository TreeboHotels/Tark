

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


class EntityAlreadyPresent(BaseException):

    def __init__(self, entity_name, payload):
        """
        raised when the user tries to create a duplicate entry of a standard entity.
        :param entity_name: the name of the entity like rule, rule_variable, policy etc.
        :param payload: the payload which was tried.
        """
        self.entity_name = entity_name
        self.payload = payload

        message = "Entity {} already present with payload {}".format(self.entity_name, self.payload)

        super(EntityAlreadyPresent, self).__init__(message)


class ResourceNotFound(BaseException):

    def __init__(self, entity_name, resource_name):
        """
        raised when the user tries to fetch a resource which is  a duplicate entry of a standard entity.
        :param entity_name: the name of the entity like rule, rule_variable, policy etc.
        :param payload: the payload which was tried.
        """
        self.entity_name = entity_name
        self.resource_name = resource_name

        message = "Entity {} not present with name {}".format(self.entity_name, self.resource_name)

        super(ResourceNotFound, self).__init__(message)

