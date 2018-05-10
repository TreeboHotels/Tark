import json

from peewee import DateTimeField, CharField, TextField, ForeignKeyField

from tark.entities.models import base, rule
from tark.rules import equation_builder


class RuleEquation(base.TimestampedModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    name = CharField(max_length=100, unique=True)
    description = TextField(null=True)
    equation = TextField(null=False)

    def update_rules_map(self, rule_map):

        rule_map_copy = dict(rule_map)

        for rule in self.rules:
            if not rule_map.get(rule.name, None):
                rule.delete_instance()
            else:
                del rule_map_copy[rule.name]

        for rule_name in rule_map_copy:
            RuleEquationToRuleMap.create(equation=self, rule=rule_map_copy[rule_name])

    def evaluate(self, filters):
        equation_dict = json.loads(self.equation)
        return equation_builder.EquationBuilder(self.rules).build_equation(equation_dict).match(filters)

    @property
    def depth(self):
        return self.rules.count()

    def save(self, *args, **kwargs):
        should_build_equation = False

        if self._get_pk_value() is None:
            should_build_equation = True
        else:
            if kwargs.get("equation") and kwargs.get("equation") != self.equation:
                should_build_equation = True

        ret_val = super(RuleEquation, self).save(*args, **kwargs)

        if should_build_equation:
            self.eq_builder = equation_builder.EquationBuilder()
            self.eq_builder.build_equation(json.loads(self.equation))
            self.update_rules_map(self.eq_builder.rule_map)

        return ret_val


class RuleEquationToRuleMap(base.TimestampedModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    equation = ForeignKeyField(RuleEquation, related_name='rules')
    rule = ForeignKeyField(rule.Rule)