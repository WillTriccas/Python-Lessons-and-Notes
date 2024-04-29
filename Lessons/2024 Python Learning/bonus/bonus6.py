# We want to start with just a contents list and a filenames list
# Our target is to create 3 files, each with their respective content populating it
import os

contents = ["Document 1 contents", "Document 2 contents", "Document 3 contents"]

filenames = ["document.txt", "table.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file_path = f"files/{filename}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directory if it doesn't exist
    with open(file_path, 'w') as file:
        file.write(content)
        file.close()





# zip is an alternative to enumerate. It does not give an index but instead just outputs both input arguments in a tuple.
# if you write two consecutive pieces of content after each other in the same file (without closing it), they will be appended after each other
# if you close the file, then write, it will write over what was previously in there

