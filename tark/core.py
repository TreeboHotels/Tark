# Expose policy
from tark.policy.policy_manager import PolicyManager as policy
from tark.policy.policy_engine import PolicyEngine as engine

# Expose action
from tark.actions.action_manager import ActionManager as action
from tark.actions.base_action import BaseAction

# Expose operators
from tark.operators.operator_manager import OperatorManager as operators

# Expose rule and rule variables
from tark.rule_variables.rule_variable_manager import RuleVariableManager as rule_variable

from tark.models.db_settings import DBSettings
from tark.models.model_setup import init_database
from tark.models.constants import DatabaseType
from tark.constants import DEFAULT_CONFIG_FILE_PATH

from tark.configuration import Configuration


class Tark(object):

    def __init__(self, config_path=DEFAULT_CONFIG_FILE_PATH):
        """Initialize the rule engine"""

        self.config = Configuration(config_file=config_path)
        db_setting = DBSettings(self.config.db_type, self.config.db_name, dict(user=self.config.db_user,
                                                                               password=self.config.db_password,
                                                                               host=self.config.db_node))
        init_database(db_setting)

