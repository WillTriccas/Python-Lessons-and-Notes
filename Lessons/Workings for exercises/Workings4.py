#defining a function where if I type foo(marry) it will return Hi Marry

def foo(Name):
    message = "Hi %s" %Name
    return message

print(foo("David"))
 

#must enclose parameters in python in quotations if they are strings otherwise it will create an error saying that your input is not defined

