import logging

from tark import constants
from tark import utils
from tark.entities.models import policy, policy_group, rule, rule_variable


logger = logging.getLogger(constants.TARK_LOGGER_PREFIX + __name__)


class PolicyManager(object):

    @staticmethod
    def generate_policy_id():
        """
        :return: policy_id
        """
        policy_id = "POL-{0}{1}".format(utils.generate_unique_id(), utils.generate_unique_id())
        return policy_id

    @classmethod
    def create_policy(cls,
                      name,
                      description,
                      policy_group,
                      rule_equation,
                      action=None,
                      action_parameters=None,
                      level=None,
                      is_active=True,
                      effective_from=None,
                      effective_to=None,
                      version_major=None):
        # add validation
        policy_dict = dict(name=name,
                           description=description,
                           policy_group=policy_group,
                           rule_equation=rule_equation,
                           action=action,
                           action_parameters=action_parameters,
                           is_active=is_active)

        if level is not None:
            policy_dict["level"] = level

        if effective_from is not None:
            policy_dict["effective_from"] = effective_from

        if effective_to is not None:
            policy_dict["effective_to"] = effective_to

        if version_major is not None:
            policy_dict["version_major"] = version_major

        return policy.Policy.create(**policy_dict)

    @classmethod
    def create_policy_group(cls, name, domain, description, rule_equation=None):
        #TODO: Add validation
        return policy_group.PolicyGroup.create(name=name,
                                               domain=domain,
                                               description=description,
                                               rule_equation=rule_equation)


