try:
    width = float(input("Enter the Rectangle Width: "))
    length = float(input("Enter the Rectangle Length"))
    
    if width == length:
        print("that looks like a square!")
        exit

    area = width*length
    print(area)
except ValueError:
    print("Please enter a number instead")

    # If conditional can be used if the output is programmatically correct but what you get is not what you want from the user
    # If conditionals are not used for catching errors but checking values
