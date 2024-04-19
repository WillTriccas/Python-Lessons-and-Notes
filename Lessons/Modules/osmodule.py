import os
import time

while True:
    if os.path.exists("Files/IKEA.txt"):
        with open("Files/IKEA.txt") as myfile:
            content = myfile.read()
            print(content)
    else:
        print("File does not exist! Please make file and try again")
    
    time.sleep(10)
