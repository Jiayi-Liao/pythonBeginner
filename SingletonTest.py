from threading import Lock

class SingletonFinal(type):
    instance=None
    lock=Lock()
    def __call__(cls, *args, **kw):
        with cls.lock:
            if not cls.instance:
                cls.instance=super(SingletonFinal, cls).__call__(*args, **kw)
        return cls.instance

    def __init__(cls, name, bases, namespace):
        super(SingletonFinal, cls).__init__(name,bases,namespace)
        for klass in bases:
            if isinstance(klass, SingletonFinal):
                print "**debug** ",name,bases,namespace
                raise TypeError(str(klass.__name__) + " is final")

class ASingleton(object):
    __metaclass__ = SingletonFinal

a=ASingleton()
b=ASingleton()
assert a is b
print(a.__class__.__name__)