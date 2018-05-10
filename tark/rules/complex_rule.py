
class ComplexRule(object):

    def __init__(self, lhs, operator, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.operator = operator

    def match(self, filters):
        return self.operator.operate(self.lhs.match(filters), self.rhs.match(filters))

    @property
    def dict(self):
        return dict(type="complex_rule", value=dict(lhs=self.lhs.dict,
                                                    operator=self.operator.NAME,
                                                    rhs=self.rhs.dict))
