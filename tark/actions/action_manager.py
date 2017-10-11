import importlib
import inspect

from tark.actions.base_action import BaseAction
from tark.exception import InvalidActionClass
from tark.models.all_models import Action


class ActionManager(object):

    @classmethod
    def add_action(cls, action_class, **kwargs):
        if not action_class or not inspect.isclass(action_class) or not issubclass(action_class, BaseAction):
            raise InvalidActionClass(action_class)

        action = Action.create(**kwargs)
        action.model_path = '{0}.{1}'.format(action_class.__module__, action_class.__name__)
        action.save()

        return action

    @classmethod
    def get_action_handler(cls, action):
        """
        return the action handler for the given action type
        :param action: 
        :return: 
        """

        if not action:
            raise KeyError("action cannot be none")

        model_class_path = action.model_path

        if not model_class_path:
            raise InvalidActionClass(model_class_path)

        module_name, class_name = model_class_path.rsplit('.', 1)
        loaded_module = importlib.import_module(module_name)

        return getattr(loaded_module, class_name)
