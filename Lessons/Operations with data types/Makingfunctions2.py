#our last function only worked with lists, so lets make the same function work with dictionaries too
#have to specify what you are using from the dictionary in the new function, these are called CONDITIONALS
#Remember that values() in a dictionary, need closed brackets after values


def mean(value):
    if isinstance(value, dict):                                     #can also write this line as if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

Head_sizes = {'Matt': 1000, 'Will': 300, 'Joe': 200}

print(mean(Head_sizes))



