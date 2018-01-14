
from tark import constants


class DBSettings(object):

    def __init__(self,
                 db_type=constants.DEFAULT_DB_TYPE,
                 db_name=constants.DEFAULT_DB_NAME,
                 db_user=constants.DEFAULT_DB_USER,
                 db_password=constants.DEFAULT_DB_PASSWORD,
                 db_node=constants.DEFAULT_DB_NODE,
                 **kwargs):
        self.db_type = db_type
        self.db_name = db_name

        # db specific config parameters
        self.db_user = db_user
        self.db_password = db_password
        self.db_node = db_node
        self.db_configuration = dict()

        if self.db_user is not None:
            self.db_configuration["user"] = self.db_user

        if self.db_password is not None:
            self.db_configuration["password"] = self.db_password

        if self.db_node is not None:
            self.db_configuration["host"] = self.db_node

        self.extra_config = dict(**kwargs)
        self.db_configuration.update(**self.extra_config)

    def get_settings(self):
        return dict(db_type=self.db_type,
                    db_name=self.db_name,
                    db_user=self.db_user,
                    db_password=self.db_password,
                    db_node=self.db_node,
                    **self.extra_config)