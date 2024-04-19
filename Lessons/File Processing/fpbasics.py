myfile = open("fruits.txt")
 
 # all the above does is create a file object for the fruits.txt file
 # if you were to run it nothing would happen

print(myfile.read())


# this is how you read a file in python

with open("fruits.txt") as myfile:
    content = myfile.read()


# this is a BETTER way of opening and reading files

with open("fruits.txt") as myfile:
    content = myfile.read()

print(content[:10])

# this will print only the first 10 of the characters in the file