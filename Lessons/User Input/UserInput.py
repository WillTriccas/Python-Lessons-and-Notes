def Weather_Condition(temperature):
    if temperature > 20:
        return "Hot"
    elif temperature < 8:
        return "Freezing"
    else:
        return "Mild"

User_Input = float(input("Enter Temperature:"))          
  
print(Weather_Condition(User_Input))                    
 
#this is how you gain an input from the user (using the input function), all user
#inputs are registered as strings so you have to convert them to ints/floats if you
#are asking the user to input a number