# challenge is to make a function that returns only ints from a list of ints and strings

def numbers(lst):
    return [items for items in lst if type(items) != str]

# lets test it

Example_List = [100, "pants", 'big boi', 92, 7.2]

print(numbers(Example_List))

