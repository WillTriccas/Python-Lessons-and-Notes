Temperatures = [214, 356, 341, 105, 72, 'Warm', 81, 'BOGUS']

New_Temps = [temps/10 for temps in Temperatures]
print(New_Temps)


# if you include an if-else conditional in your list comprehension, your FOR loop has to go at the end of your statement
# instead of at the front like above otherwise you will get a syntax error.
# Example:

Temperatures = [214, 356, 341, 105, 72, 'Warm', 81, 'BOGUS']

def foo(lst):
    return [numbers if isinstance(numbers, int) else 0 for numbers in lst]

print(foo(Temperatures))

#above works
