import wrapt


@wrapt.decorator
def log(fn, instance, args, kwargs):
    print "in"
    ret = fn(*args, **kwargs)
    print "out"
    return ret

@log
def convert(s1):
    return int(s1)

convert("123")