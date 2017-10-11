from tark.models.constants import DatabaseType


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
