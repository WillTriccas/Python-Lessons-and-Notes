prompt = "Please enter a to do: "

# We want to create the list outside of the todo While loop because otherwise it would get overriden each time
todos = []

# True is always True, so as long as you have a loop stating if something is True, it will happen

while len(todos) < 5:
    todo = input(prompt)
    todos.append(todo.capitalize())  #capitalize makes the first letter of the string a capital letter. title() method will capitalise each word in the string
    print(todos)
    print("Enter another to do: ")


# methods are attached to objects as 'attributes'. E.g. the append method is attached to the list object
# Everything outside of a loop is executed only once in Python

# To understand the methods for each datatype or object, we can use dir:

dir(str)
dir(list)
dir(todos)

# To understand what each method does, we can use the help method:

help(list.append) # for example

# You can use help and dir directly in the python terminal and dont actually put them in scripts, I just did here for an example


