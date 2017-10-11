from peewee import Model

from tark.models import config


class BaseModel(Model):
    class Meta:
        database = config.db