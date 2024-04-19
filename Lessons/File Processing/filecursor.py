# to print a file object multiple times, you have to print it as a variable over and over again

myfile = open("fruits.txt")

contents = myfile.read()

print(contents)
print(contents)
print(contents)

#this would return fruits.txt 3 times
