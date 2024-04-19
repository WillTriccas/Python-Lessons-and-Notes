# Task is to write a new file named 'first.txt' using the first 20 characters of 'fruits.txt'

with open("/Documents/Learning Python/Lessons/File Processing/differentlocation/fruits.txt", "r") as myfile:
    addon = myfile.read()
with open("/Documents/Learning Python/Lessons/Folder for text files/first.txt", "w") as mydoc:
    mydoc.write(addon[:20])


# new file will be created in folder for text files
