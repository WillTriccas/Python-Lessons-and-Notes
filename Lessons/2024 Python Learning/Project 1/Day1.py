# Always start with the simplest version of the app, then add features and details later
# Virtual environments let you have a stable, reproducible, and portable environment. You are in control of which packages versions are installed and when they are upgraded.
# Always create a venv and change the interpreter to that virtual environment for each new project
# You can have as many venvs as you want
# Create a new venv for a set of projects that share similar characteristics 

prompt = "Please enter a to do: "
User_Input1 = input(prompt)
User_Input2 = input(prompt)
User_Input3 = input(prompt)

User_Inputs = [User_Input1, User_Input2, User_Input3]

Length = len(User_Inputs)
#The above tells us the total number of to dos by measuring the length of the list

print("You currently have", Length, "To Do's")


# Every function outputs something 