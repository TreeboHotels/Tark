from tark.entities.constants import DatabaseType
from tark.rule_variables import default_rule_variables
from tark.operators import default_operators


DATETIME_FORMAT_STRING = "%Y-%m-%d %H:%M:%S.%f"

TARK_LOGGER_PREFIX = "tark"

DEFAULT_CONFIG_FILE_PATH = "/var/tmp/tark.yaml"
DEFAULT_IMPORT_PATHS = '.'

DEFAULT_APP_ID = 'DefaultApp'
DEFAULT_DB_TYPE = DatabaseType.POSTGRESQL_DATABASE
DEFAULT_DB_NAME = 'tark'
DEFAULT_DB_USER = 'root'
DEFAULT_DB_PASSWORD = ''
DEFAULT_DB_NODE = 'localhost'


class PolicyDomains(object):
    """Define all the policy domains here"""
    REFUND_POLICY = "refund_policy"

    POLICY_DOMAIN_CHOICES = (
        (REFUND_POLICY, REFUND_POLICY),
    )


class ActionTypes(object):
    """Define all the action types."""

    VALUE_CALCULATOR = "value_calculator"

    ACTION_CHOICES = (
        (VALUE_CALCULATOR, VALUE_CALCULATOR),
    )


class PolicyQueryStatus(object):
    """The list of policy query responses"""

    NO_MATCHING_POLICY = "no_matching_policy"
    CONFLICTING_POLICY = "conflicting_policy"
    QUERY_SUCCESS = "query_success"


class DefaultRuleVariableTypes(object):
    """List of default rule variable types"""

    LEBELED_INT = default_rule_variables.LabeledInt.NAME
    LABELED_FLOAT = default_rule_variables.LabeledFloat.NAME
    LABELED_STRING = default_rule_variables.LabeledString.NAME
    CONST_INT = default_rule_variables.ConstInt.NAME
    CONST_FLOAT = default_rule_variables.ConstFloat.NAME
    CONST_STRING = default_rule_variables.ConstString.NAME
    NO_OF_DAYS = default_rule_variables.NoOfDays.NAME


class DefaultComparators(object):
    """List of default comparators"""

    EQUAL = default_operators.Equal.NAME
    NOT_EQUAL = default_operators.NotEqual.NAME
    GREATER_THAN = default_operators.GreaterThan.NAME
    LESS_THAN = default_operators.LessThan.NAME
    GREATER_THAN_EQUAL = default_operators.GreaterThanEqual.NAME
    LESS_THAN_EQUAL = default_operators.LessThanEqual.NAME


class DefaultLogicalOperators(object):
    """List of default logical operators"""

    AND = default_operators.And.NAME
    OR = default_operators.Or.NAME
