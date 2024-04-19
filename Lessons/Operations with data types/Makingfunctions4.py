# making a function with an arbitrary number of keyword arguments

def foo(**kwargs):
    return kwargs

print(foo(a = 4, b = "panda", c = 2.456))


# this returns the function result as a DICTIONARY, where as a function of multiple non-keyword arguments returns a TUPLE (unless changed
# like we did in workings9.py)