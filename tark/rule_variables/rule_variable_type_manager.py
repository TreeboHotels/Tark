import importlib
import inspect

from tark.rule_variables import base_rule_variable, default_rule_variables
from tark.entities.models import rule_variable
from tark import exception


class RuleVariableTypeManager(object):

    rule_variables_mapping = {
        default_rule_variables.LabeledInt.NAME: default_rule_variables.LabeledInt,
        default_rule_variables.LabeledFloat.NAME: default_rule_variables.LabeledFloat,
        default_rule_variables.LabeledString.NAME: default_rule_variables.LabeledString,
        default_rule_variables.ConstInt.NAME: default_rule_variables.ConstInt,
        default_rule_variables.ConstFloat.NAME: default_rule_variables.ConstFloat,
        default_rule_variables.ConstString.NAME: default_rule_variables.ConstString,
        default_rule_variables.NoOfDays.NAME: default_rule_variables.NoOfDays,
    }

    @classmethod
    def register_rule_variable_type(cls, rule_variable_type_class, name, argument_keys, description):

        if cls.rule_variables_mapping.get(name, None) is not None:
            raise KeyError("rule_variable type name cannot have one of the default name {}".format(name))

        if not rule_variable_type_class or not inspect.isclass(rule_variable_type_class) \
                or not issubclass(rule_variable_type_class, base_rule_variable.BaseRuleVariableType):
            raise exception.InvalidRuleVariableTypeClass(rule_variable_type_class)

        return rule_variable.RuleVariableType.create(name=name,
                                                     argument_keys=argument_keys,
                                                     description=description,
                                                     model_path='{0}.{1}'.format(rule_variable_type_class.__module__,
                                                                                 rule_variable_type_class.__name__))

    @classmethod
    def get_rule_variable_class(cls, type):
        """
        return the action handler for the given action type
        :param type: 
        :return: 
        """

        # first search in default actions
        type_class = cls.rule_variables_mapping.get(type)

        if type_class:
            return type_class

        # now search in rule variable type db
        action_obj = rule_variable.RuleVariableType.get(name=type)

        model_class_path = action_obj.model_path

        if not model_class_path:
            raise exception.InvalidRuleVariableTypeClass(model_class_path)

        module_name, class_name = model_class_path.rsplit('.', 1)
        loaded_module = importlib.import_module(module_name)

        return getattr(loaded_module, class_name)