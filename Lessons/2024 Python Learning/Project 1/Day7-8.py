# Because we are adding our data to the external document on a new line, we are seeing an extra breakline in our python output, lets remove these
# We will remove these by editing the list, not the data in the document itself.
# We can also open and close our files in a better way, we will do that in this file, using 'with' context manager. You also dont need to close the file 

prompt = "Please type add, show, edit, complete or exit: "

while True:
    user_action = input(prompt)

    with open("../files/todos.txt",'r') as file: 
        todos = file.readlines()
    
    match user_action.strip():
        case "add":
            todo = input("Enter a to do: ") + "\n"

            todos.append(todo)

            with open('../files/todos.txt','w') as file:
                file.writelines(todos)
            
        case "show" | "display":

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

          #  new_todos = [item.strip('\n') for item in todos]    This is a list comprehension which is exactly the same as the block above (just another way of doing it)
          #  You dont have to use a list comprehension for this example, could just remove the backslash n in the for loop below (item.strip('\n'))
          #  But it is best practice when editing a list to use a list comprehension
          
            for index, item in enumerate(new_todos):
                item = item.title()
                row = f"{index + 1}-{item}"
                print(row)            
        case "edit":
            number = int(input("Please enter the number of the todo to edit: "))
            number = number - 1
            new_to_do = input("Enter the new to do: ")
            todos[number] = new_to_do + '\n'
            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)
        
        case "complete":
            number = int(input("Please enter the number of your completed to do: "))
            item_removed = todos[number-1].strip('\n') #removing the breakline here because we added it earlier so that it would appear on different lines in our output file
            todos.pop(number-1)
            with open('../files/todos.txt','w') as file:
                file.writelines(todos)
            print(f"You have successfully removed {item_removed}")

        case "exit":
            break
        case _:
            print("unknown command, please try again: ")


print("Thank you for using this to do list program!")

# List comprehensions are basically for loops within a list that makes it on the fly
# common practice to use comments to actually describe code
# Use List comprehensions over for loops where possible because it uses less code
# the open method is defaulted to r, so you dont need to include the r when reading a file, although it is good practice.
# Using the with context manager automatically closes the document at the end of the loop