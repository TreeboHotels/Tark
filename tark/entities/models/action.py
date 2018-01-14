
from peewee import DateTimeField, CharField, TextField


from tark.entities.models import base


class Action(base.TimestampedModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    name = CharField(max_length=50, unique=True)
    argument_keys = TextField()
    model_path = CharField(max_length=200, null=True)
    description = TextField(null=True)



