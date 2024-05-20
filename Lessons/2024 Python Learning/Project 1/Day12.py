# Functions can have inputs (parameters/arguments) but we have not created the functions with arguments yet. That is going to change now
# In the function definition, the input is called a parameter, when the function is called in the script, you put it with an ARGUMENT
# Take the function below, at the moment, the filename is hardcoded, so what we want to do is change that so a parameter dictates the name of the file

"""def get_todos():
    with open("../files/todos.txt",'r') as file_local: 
            todos_local = file_local.readlines()
    return todos_local"""

def get_todos(filename):
    with open(filename,'r') as file_local: 
            todos_local = file_local.readlines()
    return todos_local


prompt = """Please type add, show, edit, complete or exit.
When typing add, please immediately follow with your todo 
When typing edit or complete, type the number of the todo you wish to alter after it: """

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    
    if  user_action.startswith("add"):
        todo = user_action[4:] 

        todos = get_todos("../files/todos.txt")  # This is the function call for opening the file in read mode

        if not todo.endswith('\n'):
            todo += '\n'

        todos.append(todo)

        with open('../files/todos.txt','w') as file:
            file.writelines(todos)
        
    elif user_action.startswith("show" or "display"): 

        todos = get_todos("../files/todos.txt") # have to write the exact path to get to the file in the function call as the argument (this is maybe not a good example of using parameters in functions as it is easier to leave it how it was)
        
        new_todos = []

        new_todos = [item.strip('\n') for item in todos]    
        
        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)            
    elif user_action.startswith("edit"):
        
        try:
            todos = get_todos("../files/todos.txt")
            
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
            todos = get_todos(filename="../files/todos.txt") #you can explicitly reference the argument in the function when you call it BUT you dont have to, this is normally just for ease of reading code
            
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

