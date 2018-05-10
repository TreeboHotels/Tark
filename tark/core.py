from tark.actions import action_manager
from tark.conf.configuration import Configuration
from tark.constants import DEFAULT_CONFIG_FILE_PATH
from tark.engine import policy_engine
from tark.entities.model_setup import init_database
from tark.operators import operator_manager
from tark.policies import policy_manager
from tark.rule_variables import rule_variable_type_manager
from tark.rules import rule_manager


class Tark(object):

    def __init__(self, config_path=DEFAULT_CONFIG_FILE_PATH):
        """Initialize the rule engine"""

        self.config = Configuration(config_file=config_path)

        self.config.db = init_database(self.config.db_settings, self.config.app_id)

        self.operators = operator_manager.OperatorManager()
        self.engine = policy_engine.PolicyEngine()
        self.policies = policy_manager.PolicyManager()
        self.actions = action_manager.ActionManager()
        self.rules = rule_manager.RuleManager()
        self.rule_variable_types = rule_variable_type_manager.RuleVariableTypeManager()


