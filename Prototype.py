import copy


class SubComponent(object):
    pass


class ComplexData(object):
    def __init__(self):
        self.d1 = "abc"
        self.d2 = [1, 2, 3]
        self.d3 = SubComponent()


c = ComplexData()
copy1 = copy.copy(c)
copy2 = copy.deepcopy(c)
del c.d2[0]
