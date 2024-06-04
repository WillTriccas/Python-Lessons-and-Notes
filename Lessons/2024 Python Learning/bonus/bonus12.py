# The lesson here is to not make the output of a function complex if it doesnt need to be 
# A concept called decoupling
# The whole concept is that a function should do one thing and it should do it well
# In this example, we are grabbing feet and inches from a single input and then converting this to metres
# instead, we will change this to two functions, one that returns feet and inches and one that converts this to metres
# if you want to make quality functions, you need to make your functions as simple as possible and decouple as much as possible

feet_and_inches = input("Enter Feet and Inches: ")

def parse(feet_and_inches):
    parts = feet_and_inches.split(" ")   # What split does, is it splits the string based on the string you put in the split method, therefore it will split the string on every space and create a list
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
    

def convert(feet, inches):
    metres = feet * 0.3048 + inches * 0.0254
    return metres 

parsed = parse(feet_and_inches)
result = (convert(parsed['feet'], parsed['inches']))

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} metres ")

if result < 1.2:
    print("Child is too small to ride")
else:
    print("You are tall enough to ride")