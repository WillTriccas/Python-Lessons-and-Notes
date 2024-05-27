# Sometimes when we should assign a default argument to the functions we make. 
# That means we dont have to assign an argument every time we call the function 
# BUT, if we want something other than the default argument ,we can put this in the function call and it will overwrite the default argument
# You can also describe what a function does as a 'doc-string', this is written in the first line of the function definition
# The doc string is revealed when someone uses the 'help' function on your function
# Especially useful when you have different python scripts talking to eachother and want clarity on what functions do

def get_todos(filepath="../files/todos.txt"):   #this is the default argument being defined here
    """ Read a text file and return the         
    list of to-do items.
    """
    with open(filepath,'r') as file_local: 
            todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="../files/todos.txt"): # Non-default args cant follow default args so need to re-adjust
    """ Write the to-do items list in the text file  """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)  


prompt = """Please type add, show, edit, complete or exit.
When typing add, please immediately follow with your todo 
When typing edit or complete, type the number of the todo you wish to alter after it: """

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    
    if  user_action.startswith("add"):
        todo = user_action[4:] 

        todos = get_todos()  

        if not todo.endswith('\n'):
            todo += '\n'

        todos.append(todo)

        write_todos(todos)  
        
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

            write_todos(todos)

        except ValueError:                  
            print("That command was not valid, please enter the number of the todo you want to edit")
            continue  
    
    elif "complete" in user_action:
        try:
            todos = get_todos() 
            
            number = int(user_action[9:])
            item_removed = todos[number-1].strip('\n') 
            todos.pop(number-1)
            write_todos(todos)
            print(f"You have successfully removed {item_removed}")

        except IndexError: 
            print("That number is out of range")
            continue

    elif "exit" in user_action:
        break
    else:
        print("unknown command, please try again: ")


print("Thank you for using this to do list program!")

