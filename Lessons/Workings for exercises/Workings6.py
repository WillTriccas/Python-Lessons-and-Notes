#Loop Workings
# Want to just return numbers over 50

colors = [11, 34, 98, 43, 45, 54, 54]
for numbers in colors:
    if numbers > 50:
        print(numbers)

## This below is just to return items that are ints

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for numbers in colors:
    if type(numbers) == int:
        print(numbers)


### This below just return items that are ints AND above 50

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for numbers in colors:
    if type(numbers) == int and numbers > 50:
        print(numbers)