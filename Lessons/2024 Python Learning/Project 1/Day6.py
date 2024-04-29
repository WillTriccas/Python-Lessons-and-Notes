# Now we are going to start storing the data, so it isnt lost everytime

prompt = "Please type add, show, edit, complete or exit: "

while True:
    user_action = input(prompt)

    file = open("../files/todos.txt",'r')
    todos = file.readlines()
    file.close()
    
    match user_action.strip():
        case "add":
            todo = input("Enter a to do: ") + "\n"

            todos.append(todo)

            file = open('../files/todos.txt','w')
            file.writelines(todos)
            file.close()
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
            file = open("../files/todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case "complete":
            number = int(input("Please enter the number of your completed to do: "))
            item_removed = todos[number-1]
            todos.pop(number-1)
            file = open('../files/todos.txt','w')
            file.writelines(todos)
            file.close()
            print(f"You have successfully removed {item_removed}")
        case "exit":
            break
        case _:
            print("unknown command, please try again: ")


print("Thank you for using this to do list program!")

# We have added "\n" when adding a to do as this adds a breakline to our database(text file in this instance)
# to write input to an external file, we use the open method and state we want to write to it
# to not continually overrite our file with a new list every time we start the program, we need to open the existing file and write to that. This is done through read mode. DELETE THE LIST
# When we have opened a file object, we need to ensure that it is closed afterwards (this is good practice so that other parts of code dont interfere with it)
# Needed to open the file outside of the match block because if I asked to show first and the todos variable hadnt been created, it threw an error
# You never normally create a list manually in python file, you get a list from using an external file. You can check the type of an external file with type(external_file_variable)
# If the path of the file we want to use is not in the same folder, we have to point python at that folder
# If you are putting in the absolute path of a file (straight from your computer path) put an 'r' before the string containing the path so that any special characters are ignored.
