 # how to make a function that can have an arbitrary number of non-keyword arguments (not a set amount like 1 or two)

def func(*args):
    return sum(args) / len(args)

print(func(3, 4, 5, 6, 7))

