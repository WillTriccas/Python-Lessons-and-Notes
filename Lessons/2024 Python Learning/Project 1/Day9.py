# Up to this point, we have used the Match/Case function, but this wont always work
# We now want to make a statement for adding a to do a single request. Not add, then waiting to add a new to do which it currently has
# We can use the 'in' operator, we can find out if the user wants to do something in one statement. 
# Cant use 'in' with match and case

prompt = """Please type add, show, edit, complete or exit. 
When typing edit or complete, type the number of the todo you wish to alter after it: """

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    
    if "add" in user_action:
        todo = user_action[4:] # We dont need to ask for another input if they are adding it straight away, so we use list slicing to extract all the characters after the instruction

        with open("../files/todos.txt",'r') as file: 
            todos = file.readlines()

        if not todo.endswith('\n'):
            todo += '\n'

        todos.append(todo)

        with open('../files/todos.txt','w') as file:
            file.writelines(todos)
        
    elif "show" in user_action or "display" in user_action: # We want to add elifs because otherwise it will check each block indepently (if it was an 'if)
                                                            # or is a comparison operator we can use to take more inputs
        with open("../files/todos.txt",'r') as file: 
            todos = file.readlines()
        
        new_todos = []

        new_todos = [item.strip('\n') for item in todos]    
        
        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)            
    elif "edit" in user_action:
        
        with open("../files/todos.txt",'r') as file: 
            todos = file.readlines()
        
        number = int(user_action[5:])
        number = number - 1
        new_to_do = input("Enter the new to do: ")
        todos[number] = new_to_do + '\n'

        with open("../files/todos.txt", 'w') as file:
            file.writelines(todos)
    
    elif "complete" in user_action:
        
        with open("../files/todos.txt",'r') as file: 
            todos = file.readlines()
        
        number = int(user_action[9:])
        item_removed = todos[number-1].strip('\n') #removing the breakline here because we added it earlier so that it would appear on different lines in our output file
        todos.pop(number-1)
        with open('../files/todos.txt','w') as file:
            file.writelines(todos)
        print(f"You have successfully removed {item_removed}")

    elif "exit" in user_action:
        break
    else:
        print("unknown command, please try again: ")


print("Thank you for using this to do list program!")


# If you highlight an entire block and do shift tab, it unindents it
# With if and elif, it matters in the order you have ordered the functions in your script. It makes sense to have the most popular cases at the top
