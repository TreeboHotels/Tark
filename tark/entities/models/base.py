import datetime

from peewee import Model


class TimestampedModel(Model):
    def save(self, *args, **kwargs):
        if self._get_pk_value() is None:
            # this is a create operation, set the date_created field
            self.created_at = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
        self.updated_at = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")
        return super(TimestampedModel, self).save(*args, **kwargs)