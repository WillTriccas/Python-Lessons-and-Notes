Student_GradesList = [8, 9, 10,5]

#above is the example of a list, however, if we want to assign an identity (a key) to our data, we can use a dictionary

Student_GradesDict = {"Will": 8, "James": 9, "Joe": 10.5}

mysum = sum(Student_GradesDict.values())
mylength = len(Student_GradesDict)
myave = mysum / mylength

print(myave)

# when calculating mysum, have to be specific when using dictionarys otherwise wont know what to sum together

print(Student_GradesDict.keys())


#this when printed will display the names of the people who got the grades - type into python shell to see