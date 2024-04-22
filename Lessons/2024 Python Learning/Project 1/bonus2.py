# Using a while loop to output 1,2,3,4,5,6

x = 1

while x <= 6:
    print(x)
    x = x + 1

# Using a while loop to obtain the correct password 

password = input("Please enter your password: ")

while password != "password":
    password = input("Incorrect password, please try again: ")

print("That is the correct password!")