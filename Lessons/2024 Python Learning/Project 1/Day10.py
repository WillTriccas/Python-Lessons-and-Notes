# Currently, if we have add or edit or complete (or any command) in the same statement from the user, our code could get confused
# For example, if had a todo which was 'add todos' if we put edit add todos, this would add another todo called add todos because add also appears in the statement
# To fix this, we want to adjust our if statements to have them check if it .startswith()
# We also want to change our code to allow the user to edit the todo they want without putting the number, but straight away putting the to do 
# At the moment this doesnt work because it is expecting an INT. We need to add a try and except block

prompt = """Please type add, show, edit, complete or exit. 
When typing edit or complete, type the number of the todo you wish to alter after it: """

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    
    if  user_action.startswith("add"):
        todo = user_action[4:] 

        with open("../files/todos.txt",'r') as file: 
            todos = file.readlines()

        if not todo.endswith('\n'):
            todo += '\n'

        todos.append(todo)

        with open('../files/todos.txt','w') as file:
            file.writelines(todos)
        
    elif user_action.startswith("show" or "display"): 

        with open("../files/todos.txt",'r') as file: 
            todos = file.readlines()
        
        new_todos = []

        new_todos = [item.strip('\n') for item in todos]    
        
        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)            
    elif user_action.startswith("edit"):
        
        try:
            with open("../files/todos.txt",'r') as file: 
                todos = file.readlines()
            
            number = int(user_action[5:])
            number = number - 1
            new_to_do = input("Enter the new to do: ")
            todos[number] = new_to_do + '\n'

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:                  # Put the error you are excepting here. This one occurs when someone puts a string after edit. We want to give them the option to fix their error so we give them the prompt again
            print("That command was not valid, please enter the number of the todo you want to edit")
            continue  #This runs another cycle of the While loop, so puts it back at the start, igores everything underneath
    
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


