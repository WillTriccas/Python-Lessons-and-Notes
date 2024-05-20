# To avoid repetitive and redundant code, we need to create custom functions
# These are normally made outside of the mainblock of code
# We are going to create a function which gets rid of the file with context managers
# good to have 2 breaklines between functions and rest of code
# function call, ALWAYS returns what is put in the return part of the function. If you dont have return defined, Python will return 'None'

def get_todos():
    with open("../files/todos.txt",'r') as file_local: 
            todos_local = file_local.readlines()
    return todos_local # Need to actively return the todos variable so when the function is called it is directly referenced
                        # change the name to todos_local because todos is a variable in the programme already (not a big issue and doesnt affect code but is the best practice)


prompt = """Please type add, show, edit, complete or exit. 
When typing edit or complete, type the number of the todo you wish to alter after it: """

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    
    if  user_action.startswith("add"):
        todo = user_action[4:] 

        todos = get_todos()  # This is the function call for opening the file in read mode

        if not todo.endswith('\n'):
            todo += '\n'

        todos.append(todo)

        with open('../files/todos.txt','w') as file:
            file.writelines(todos)
        
    elif user_action.startswith("show" or "display"): 

        todos = get_todos()
        
        new_todos = []

        new_todos = [item.strip('\n') for item in todos]    
        
        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)            
    elif user_action.startswith("edit"):
        
        try:
            todos = get_todos()
            
            number = int(user_action[5:])
            number = number - 1
            new_to_do = input("Enter the new to do: ")
            todos[number] = new_to_do + '\n'

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:                  
            print("That command was not valid, please enter the number of the todo you want to edit")
            continue  
    
    elif "complete" in user_action:
        try:
            todos = get_todos()
            
            number = int(user_action[9:])
            item_removed = todos[number-1].strip('\n') 
            todos.pop(number-1)
            with open('../files/todos.txt','w') as file:
                file.writelines(todos)
            print(f"You have successfully removed {item_removed}")

        except IndexError: 
            print("That number is out of range")
            continue

    elif "exit" in user_action:
        break
    else:
        print("unknown command, please try again: ")


print("Thank you for using this to do list program!")


# You can view how each of the functions that were built into python were made
# This is done through right clicking on the function and pressing 'go to definition'
# variables that are stored inside functions are LOCAL variables and the script wont recognise them outside of the function
