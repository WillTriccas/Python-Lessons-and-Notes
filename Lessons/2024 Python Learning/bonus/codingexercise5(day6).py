#1. prompts the user to enter a new member.
#2. adds that member the end of the existing members. For example, the user here has entered the member Solomon Right.

member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()

# key takeaway here is to read the file and save that as a variable should I want to edit it (just like in our program). This basically initiates the list