
while True:

    entered_password = input("""Please enter a new password.
Your password must contain, uppercase letters, lowercase letters and numbers: """)

    result = {}

    if len(entered_password) >=8:
        result["Length"] = True
    else:
        result["Length"] = True      # We are assigning a value to the key 'Length' in the results dictionary

    digit = False
    for i in entered_password:   #isdigit checks if argument is a digit. Although, if it is a string and a digit, it will say false. To stop this we need to iterate over full password
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in entered_password:
        if i.isupper():         # is upper is the same as is digit but checks if character is upper case
            uppercase = True

    result["uppercase"] = uppercase

    if all(result.values()) == True:    # 'all' checks if all of the values in a list are true or not.
        print("Strong Password")
        break
    else:
        print("Weak Password, try again")


