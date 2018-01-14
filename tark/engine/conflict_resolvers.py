
from abc import abstractmethod


class BaseResolver(object):

    @abstractmethod
    def resolve(self, policies):
        """
        abstart function to be overridded by all overriding class
        :return: 
        """
        pass

class DepthPriorityResolver(BaseResolver):

    NAME = "depth"

    def resolve(self, policies):
        selected_policies = []
        highest_depth = 0

        for policy in policies:
            depth = policy.rule_equation.depth
            if depth > highest_depth:
                highest_depth = depth
                selected_policies = [policy]
            elif depth == highest_depth:
                selected_policies.append(policy)
        return selected_policies


class LevelPriorityResolver(BaseResolver):

    NAME = "level"

    def resolve(self, policies):
        selected_policies = []
        highest_level = 0

        for policy in policies:
            level = policy.level
            if level > highest_level:
                highest_level = level
                selected_policies = [policy]
            elif level == highest_level:
                selected_policies.append(policy)
        return selected_policies


class ConflictResolvers(object):
    """Define conflict resolvers for policy conflict resolution"""

    DEPTH_RESOLVER = DepthPriorityResolver.NAME
    LEVEL_RESOLVER = LevelPriorityResolver.NAME

    resolver_map = {
        DEPTH_RESOLVER: DepthPriorityResolver,
        LEVEL_RESOLVER: LevelPriorityResolver
    }

    @classmethod
    def resolve(cls, policies, resolver_name=DEPTH_RESOLVER):

        resolver = cls.resolver_map(resolver_name)

        if not resolver:
            KeyError("Unsupported resolver: {}".format(resolver_name))

        return resolver().resolve(policies)