filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1) # this code replaces the '.' character with a '-' character but ONLY for the 1st instance of this character
    print(filename)

# Tuple is an immutable version of a list 

filenames1 = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")

# Rarely will you use tuples, UNLESS YOU ABSOLUTELY DONT WANT THEM TO BE CHANGED
