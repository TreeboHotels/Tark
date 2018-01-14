import logging
import json

from peewee import DateTimeField, CharField, TextField

from tark.entities.models import base
from tark.rule_variables import rule_variable_type_manager

logger = logging.getLogger(__name__)


class RuleVariableType(base.TimestampedModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    name = CharField(max_length=50, unique=True)
    argument_keys = TextField()
    model_path = CharField(max_length=200, null=True)
    description = TextField(null=True)


class RuleVariable(base.TimestampedModel):

    created_at = DateTimeField()
    updated_at = DateTimeField()
    name = CharField(max_length=50, unique=True)
    type = CharField(max_length=100)
    args = TextField(null=True)

    def object(self, value_list=None):
        """
        return the rule variable obj for the given type
        :param value_list: the list of values to searched for values to be passed to rule variable
        :return: the rule variable of given type
        """
        rule_variable_class = rule_variable_type_manager.RuleVariableTypeManager.get_rule_variable_class(self.type)

        if not rule_variable_class:
            raise KeyError("No rule variable found for given type: {}".format(self.type))

        return rule_variable_class(json.loads(self.args), value_list)

