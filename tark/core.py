from tark.conf.configuration import Configuration

from tark.constants import DEFAULT_CONFIG_FILE_PATH
from tark.entities.model_setup import init_database
from tark.operators import operator_manager


class Tark(object):

    def __init__(self, config_path=DEFAULT_CONFIG_FILE_PATH):
        """Initialize the rule engine"""

        self.config = Configuration(config_file=config_path)

        self.config.db = init_database(self.config.db_setting, self.config.app_id)

        self.operators = operator_manager.OperatorManager()

