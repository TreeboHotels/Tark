import json

from tark.entities.models import rule, rule_variable, rule_equation


class RuleManager(object):

    @classmethod
    def create_rule(cls, name, lhs, comparator, rhs, description=''):
        #TODO:: Add validation
        return rule.Rule.create(name=name, lhs=lhs, comparator=comparator, rhs=rhs, description=description)

    @classmethod
    def create_rule_variable(cls, name, type, args=None):
        """
        
        :param name: name of the rule variable
        :param type: The type of rule variable. can be either one of default rule variable or a custom one.
        :param args: type dict. the set of arguments which are needed by rule variable type.
        :return: rule variable object
        """
        return rule_variable.RuleVariable.create(name=name,
                                                 type=type,
                                                 args=json.dumps(args) if args is not None else '')

    @classmethod
    def create_rule_equation(cls, name, description, equation):
        """
        
        :param name: name of the equation
        :param description: description about the rule equation
        :param equation: The rule equation described in json.
        :return: rule equation object.
        """
        return rule_equation.RuleEquation.create(name=name,
                                                 description=description,
                                                 equation=json.dumps(equation))
