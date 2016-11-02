import wrapt


class Data(object):
    def __init__(self):
        self.d1 = "1"
        self.d2 = "hello world"

    def change1(self):
        self.d1 = "123"

    def change2(self, new_val):
        self.d2 = new_val


@wrapt.decorator
def ob1(fn, instance, *args):
    attr, val = args[0]
    ret = fn(attr, val)
    print "ob1: ", attr, " is changed to: ", val
    return ret


@wrapt.decorator
def ob2(fn, instance, *args):
    attr, val = args[0]
    ret = fn(attr, val)
    print "ob2: ", attr, " is changed to: ", val
    return ret


def add_ob(cls, ob):
    cls.__setattr__ = ob(cls.__setattr__)


add_ob(Data, ob1)
add_ob(Data, ob2)

x, y = Data(), Data()

x.d1="abc"
x.d2="hello data"
x.d3=123

y.d1="xxx"



