prompt = "Type add, show, edit or exit: "

todos = []

while True:
    user_action = input(prompt)
    
    match user_action.strip():
        case "add":
            todo = input("Enter a to do: ")
            todos.append(todo)
        case "show" | "display":
            for i in todos:
                i = i.title()
                print(i)            
        case "edit":
            number = int(input("Please enter the number of the todo to edit: "))
            number = number - 1
            new_to_do = input("Enter the new to do: ")
            todos[number] = new_to_do
        case "exit":
            break
        case _:
            print("unknown command, please try again: ")


print("Thank you for using this to do list program!")

# The match statement is another block, this essentially maps each case, as we type it out, to a specific action
# the break clause, breaks the while loop.
# for loop takes individual item in the list and prints it out
# the strip method gets rid of any whitespace we may have in our entry so that our program still interprets the answer
# | bitwise operator which essentially acts as OR
# title method capitalises each of the words in the statement entered
# common syntax for else operators in case block to have '_' as the alternative which outlines a case you have not accounted for. This HAS to be the last case argument

# Day 4

# in the edit argument, we need to ensure that our entered number is an integer
# when doing list indexing, we need to minus 1 to get the actual number of the todo in the list (because of number 1)
# We can use the list indexing to put the edited input into a specific part of the list
# float converts strings to decimal numbers, int turns strings to numbers
# to get the index number of an item in a list you simply do mylist.index("string of integer that you are looking for in the list")
# equivalent list methods: mylist.__setitem__(1, "new value") is the same as mylist[1] = "new value"



