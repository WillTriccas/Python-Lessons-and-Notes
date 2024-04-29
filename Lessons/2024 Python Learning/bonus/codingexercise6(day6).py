filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"bonus/exercise_outputs/{filename}",'w')
    file.write("Hello")
    file.close()