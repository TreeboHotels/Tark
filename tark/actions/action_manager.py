import importlib
import inspect

from tark.actions import base_action
from tark.exception import InvalidActionClass
from tark.entities.models import action
from tark import exception


class ActionManager(object):

    default_actions = {

    }

    @classmethod
    def register_action(cls, action_class, name, argument_keys, description):

        if cls.default_actions.get(name, None) is not None:
            raise KeyError("action cannot have one of the default actions name {}".format(name))

        if not action_class or not inspect.isclass(action_class) or not issubclass(action_class, base_action.BaseAction):
            raise exception.InvalidActionClass(action_class)

        return action.Action.create(name=name,
                               argument_keys=argument_keys,
                               description=description,
                               model_path='{0}.{1}'.format(action_class.__module__, action_class.__name__))


    @classmethod
    def get_action(cls, action_name):
        """
        return the action handler for the given action type
        :param action: 
        :return: 
        """

        # first search in default actions
        action_obj = cls.default_actions.get(action_name)

        if action_obj:
            return action_obj

        # now search in actions db
        action_obj = action.Action.get(name=action_name)

        model_class_path = action_obj.model_path

        if not model_class_path:
            raise InvalidActionClass(model_class_path)

        module_name, class_name = model_class_path.rsplit('.', 1)
        loaded_module = importlib.import_module(module_name)

        return getattr(loaded_module, class_name)
