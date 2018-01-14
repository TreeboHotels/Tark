from peewee import DateTimeField, CharField, TextField, ForeignKeyField

from tark.entities.models import base, rule_equation


class PolicyGroup(base.TimestampedModel):

    DEFAULT_DOMAIN = 'general'

    created_at = DateTimeField()
    updated_at = DateTimeField()
    name = CharField(max_length=100, unique=True)
    domain = CharField(max_length=50, default=DEFAULT_DOMAIN)
    description = TextField(null=True)
    rule_equation = ForeignKeyField(rule_equation.RuleEquation, null=True)

    def match(self, filters):
        is_match = True
        if self.rule_equation:
            is_match = self.rule_equation.evaluate(filters)

        return is_match


