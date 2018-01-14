import json

from peewee import DateTimeField, CharField, TextField, IntegerField, ForeignKeyField, BooleanField

from tark.entities.models import base, action, policy_group, rule_equation
from tark.engine import policy_manager
from tark.actions import action_manager


class PolicyArchive(base.TimestampedModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    effective_from = DateTimeField(null=True)
    effective_to = DateTimeField(null=True)
    name = CharField(max_length=100)
    policy_id = CharField(max_length=50)
    version_major = IntegerField(default=1)
    version_minor = IntegerField(default=0)
    description = TextField(null=True)
    level = IntegerField(default=1)
    action = CharField(max_length=100)
    action_parameters = TextField(null=True)
    policy_group = ForeignKeyField(policy_group.PolicyGroup, null=True, related_name='policy_archives')
    rule_equation = ForeignKeyField(rule_equation.RuleEquation)


class Policy(base.TimestampedModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    effective_from = DateTimeField(null=True)
    effective_to = DateTimeField(null=True)
    name = CharField(max_length=100)
    policy_id = CharField(max_length=50)
    version_major = IntegerField(default=1)
    version_minor = IntegerField(default=0)
    description = TextField(null=True)
    is_active = BooleanField(default=True)
    action = ForeignKeyField(action.Action)
    action_parameters = TextField(null=True)
    level = IntegerField(default=1)
    policy_group = ForeignKeyField(policy_group.PolicyGroup, null=True, related_name='policies')
    rule_equation = ForeignKeyField(rule_equation.RuleEquation)

    def save(self, *args, **kwargs):
        if self._get_pk_value() is None:
            if kwargs.get("policy_id", None) is None:
                self.policy_id = policy_manager.PolicyManager.generate_policy_id()
        else:
            # Create a copy of the policy to archive
            self.archive()
            # update minor version
            self.version_minor += 1
        return super(Policy, self).save(*args, **kwargs)

    def archive(self):
        archive_obj = PolicyArchive.create(effective_from=self.effective_from,
                             effective_to=self.effective_to,
                             name=self.name,
                             policy_id=self.policy_id,
                             version_major=self.version_major,
                             version_miinor=self.version_minor,
                             description=self.description,
                             action=self.action,
                             level=self.level,
                             action_parameters=self.action_parameters,
                             rule_equation=self.rule_equation,
                             policy_group=self.policy_group)

        return archive_obj

    @property
    def version(self):
        return "{}.{}".format(self.version_major, self.version_minor)

    def match(self, filters):
        is_match = True
        if self.rule_equation:
            is_match = self.rule_equation.evaluate(filters)

        return is_match

    def act(self, arguments, filters):
        """
        Acts on the action defined
        :param arguments: 
        :param filters: 
        :return: 
        """

        if type(arguments) == str:
            arguments = json.loads(arguments)

        action = action_manager.ActionManager.get_action_handler(self.action)

        return_val = action.act(arguments, filters)

        return return_val

