 # making a function that returns as many strings as you put into it as completely capitalised strings in a list

def Uppercase_maker(*args):
    args = [words.upper() for words in args]
    return args

print(Uppercase_maker("hello", "you", "dirty", "cunt"))


# to return the uppercase strings in order alphabetically (or ascending order), you have to put return sorted(args)


