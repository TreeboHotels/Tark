

from tark.models.constants import DatabaseType
from tark.models import config
from tark.models.base_model import BaseModel
from tark.models.all_models import Policy, Rule, PolicyToRulesMap, RuleVariable, Operator, Action

models_list = [Policy, Rule, PolicyToRulesMap, RuleVariable, Operator, Action]


def init_database(db_settings):
    """
    Initialze the database
    :param db_settings: 
    :return: 
    """

    db_handler = DatabaseType.db_mapping.get(db_settings.db_type)

    if not db_handler:
        raise KeyError("Invalid db type: {}".format(db_settings.db_type))

    config.db = db_handler(db_settings.db_name, db_settings.db_configuration)

    for model in models_list:
        model._meta.database = config.db

    config.db.connect()

    config.db.create_tables(models_list, safe=True)


