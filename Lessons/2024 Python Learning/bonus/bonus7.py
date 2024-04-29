# We want to use a list comprehension to take the entries in the filenames list, replace the . with a - and concatonate a .txt at the end

filenames = ["1.doc","1.report","1.presentation"]

filenames =[filename.replace('.','-') +'.txt' for filename in filenames]

print(filenames)