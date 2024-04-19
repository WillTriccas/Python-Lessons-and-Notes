import time

while True:
    with open("Hello.txt","r") as testfile:
        content = testfile.read()
        print(content)
        time.sleep(10)


# this will run until an error is encountered - eg if the file you are looking for to print is deleted. If the file returns,
# the script will not begin to run again like this, you need to import the 'os' module and use a function from that to make that happen.
