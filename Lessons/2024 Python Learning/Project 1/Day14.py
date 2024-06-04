# When programs get a lot bigger, they will often have a lot of functions. It is often best practice to put logical parts of the code (functions) in separate documents
# Now, we are going to write all of our functions in a separate file, IN THE SAME DIRECTORY. This is called a module
# We dont HAVE to import specific functions from a module. We can just refer to them implicitly in the program like todos = functions.get_todos(), if we just said import functions
# if the module was in a different directory, you need to reference that directory eg from modules import functions 


# Additional anatomy of python key to know - Classes/types in python enable you to produce instances of that class output in your program
# example includes lists. THey are all different but belong to the same class/type.
# Many classes in python are just created by other people and you can use them but also possible to make your own classes.

from functions import get_todos, write_todos


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

