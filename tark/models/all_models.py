from peewee import CharField, TextField, ForeignKeyField, IntegerField

from tark.models.base_model import BaseModel


class RuleVariable(BaseModel):
    name = CharField(max_length=50)
    type = CharField(max_length=100)
    argument_list = TextField(null=True)
    model_path = CharField(max_length=200, null=True)


class Action(BaseModel):
    name = CharField(max_length=50)
    type = CharField(max_length=50)
    key_list = TextField()
    description = TextField(null=True)
    argument_list = TextField()
    model_path = CharField(max_length=200, null=True)


class Operator(BaseModel):
    name = CharField(max_length=50)
    description = TextField(null=True)
    model_path = CharField(max_length=200, null=True)


class PolicyGroup(BaseModel):
    name = CharField(max_length=100)
    domain = CharField(max_length=50)
    description = TextField(null=True)


class Policy(BaseModel):
    name = CharField(max_length=100)
    description = TextField(null=True)
    action = ForeignKeyField(Action)
    action_parameters = TextField(null=True)
    policy_group = ForeignKeyField(PolicyGroup)


class Rule(BaseModel):
    name = CharField(max_length=100)
    description = TextField(null=True)
    comparator = ForeignKeyField(Operator)
    operand_one = ForeignKeyField(RuleVariable, related_name='operand_one')
    operand_one_values = TextField(null=True)
    operand_two = ForeignKeyField(RuleVariable, related_name='operand_two')
    operand_two_values = TextField(null=True, )


class PolicyToRulesMap(BaseModel):
    policy = ForeignKeyField(Policy)
    rule = ForeignKeyField(Rule)
    order = IntegerField(null=True)


class PolicyGroupToRulesMap(BaseModel):
    policy_group = ForeignKeyField(PolicyGroup)
    rule = ForeignKeyField(Rule)
    order = IntegerField(null=True)




