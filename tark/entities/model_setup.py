

from tark.entities.constants import DatabaseType
from tark.entities.models.policy import Policy, PolicyArchive
from tark.entities.models.policy_group import PolicyGroup
from tark.entities.models.rule_equation import RuleEquation, RuleEquationToRuleMap
from tark.entities.models.action import Action
from tark.entities.models.rule_variable import RuleVariable
from tark.entities.models.rule import Rule

models_list = [Policy, Rule, RuleVariable, RuleEquation, RuleEquationToRuleMap, Action, PolicyGroup, PolicyArchive]


def init_database(db_settings, app_name="default"):
    """
    Initialze the database
    :param db_settings: 
    :param app_name
    :return: 
    """

    db_handler = DatabaseType.db_mapping.get(db_settings.db_type)

    if not db_handler:
        raise KeyError("Invalid db type: {}".format(db_settings.db_type))

    db = db_handler(db_settings.db_name, db_settings.db_configuration)

    for model in models_list:
        model._meta.database = db
        model._meta.db_table = app_name.lower() + "_tark_" + model.__name__.lower()

    db.connect()

    db.create_tables(models_list, safe=True)

    return db


