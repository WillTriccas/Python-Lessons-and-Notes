 # appending one text file to another requires the open() function to be in "a" mode
 # to append one file, you have to have opened it before with a separate open function so that it is saved in memory and can be quickly used in the script

with open("Doc1.txt", "r") as myfile:
     content = myfile.read()

with open("Doc2.txt", "a+") as mydoc:
    mydoc.write(content)
    mydoc.seek(0)
    print(mydoc.read())

