waiting_list = ["sean", "ben", "john"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

# Working with the enumerate function
# lists are mutable, therefore when we apply a function/method to a list, we dont need to create a new variable for it to apply
# (the above is unlike strings)
# You have to use as many variables as there are items in the internal tuples or lists
# The enumerate function ALWAYS produces a sequence of tuples each containing two items. Therefore, when using enumerate, you have to use two variables, not less, not more
