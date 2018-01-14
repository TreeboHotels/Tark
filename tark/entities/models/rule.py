import logging

from peewee import DateTimeField, CharField, TextField, ForeignKeyField

from tark.entities.models import base, rule_variable
from tark.operators import operator_manager

logger = logging.getLogger(__name__)


class Rule(base.TimestampedModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    name = CharField(max_length=100, unique=True)
    description = TextField(null=True)
    lhs = ForeignKeyField(rule_variable.RuleVariable, related_name='lsh_rules')
    rhs = ForeignKeyField(rule_variable.RuleVariable, related_name='rhs_rules')
    comparator = CharField(max_length=100)

    def match(self, filters):
        is_a_match = False
        try:
            is_a_match = operator_manager.OperatorManager.get_comparator(self.comparator)\
                .operate(self.lhs.object(filters), self.rhs.object(filters))
        except Exception as e:
            logger.warning("unable to evaluate rule with id {} with reason {} .".format(self.id, str(e)))

        return is_a_match

    @property
    def dict(self):
        return dict(type="rule", value=dict(name=self.name))

