prompt = "Please type add, show, edit, complete or exit: "

todos = []

while True:
    user_action = input(prompt)
    
    match user_action.strip():
        case "add":
            todo = input("Enter a to do: ")
            todos.append(todo)
        case "show" | "display":
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index + 1}-{item}"
                print(row)            
        case "edit":
            number = int(input("Please enter the number of the todo to edit: "))
            number = number - 1
            new_to_do = input("Enter the new to do: ")
            todos[number] = new_to_do
        case "complete":
            number = int(input("Please enter the number of your completed to do: "))
            item_removed = todos[number-1]
            todos.pop(number-1)
            print(f"You have successfully removed {item_removed}")
        case "exit":
            break
        case _:
            print("unknown command, please try again: ")


print("Thank you for using this to do list program!")


# The enumerate function returns the list index number for each item in a list. If we want to return both the enumerated index and the item
# we need to look for and return 2 variables in our for loop (as above)
# after just adding the above changes, we have a fair bit of white space which we cant currently remove but it looks bad. To get rid of that, we can use f strings
# f strings, as above, are a way to control strings and their spaces more effectively
# specifying minus indicies, works backwards on the list. Eg, -1 index is the last item