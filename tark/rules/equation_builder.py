
from tark.entities.models import rule
from tark.operators import operator_manager
from tark.rules import complex_rule


class EquationBuilder(object):

    def __init__(self, rule_mappings=None):
        rule_map = dict()
        if rule_mappings is not None:
            for rule_map_entry in rule_mappings:
                rule_obj = rule_map_entry.rule
                rule_map[rule_obj.name] = rule_obj

        self.rule_map = rule_map

    def build_equation(self, equation_dict):
        return self.get_rule_entity_from_dict(equation_dict)

    def get_rule_entity_from_dict(self, dict_obj):

        type = dict_obj.get("type")

        if type == "rule":
            rule_obj = self.get_rule_from_dict(dict_obj["value"])
        elif type == "complex_rule":
            rule_obj = self.get_complex_rule_from_dict(dict_obj["value"])
        else:
            raise KeyError("Invalid rule_entity_type: {}".format(type))

        return rule_obj

    def get_rule_from_dict(self, dict_obj):
        rule_name = dict_obj["name"]
        rule_obj = self.rule_map.get(dict_obj["name"], None)

        if not rule_obj:
            rule_obj = rule.Rule.get(name=rule_name)
            self.rule_map[rule_obj.name] = rule_obj
        return rule_obj

    def get_complex_rule_from_dict(self, dict_obj):
        lhs_obj = self.get_rule_entity_from_dict(dict_obj["lhs"])
        rhs_obj = self.get_rule_entity_from_dict(dict_obj["rhs"])
        operator = operator_manager.OperatorManager.get_logic_operator(dict_obj["operator"])
        return complex_rule.ComplexRule(lhs_obj, operator, rhs_obj)


