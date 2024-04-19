# Challenge is to define a function where you take a single string character and a filepath as its parameters and it returns the amount
# of times that the character as the parameter appears in the file

def foo(character, filpath):
     filepath = "bear.txt"
     with open(filepath) as myfile:
         content = myfile.read()
     return content.count(character)
         