import os
import time
import pandas

while True:
    if os.path.exists("Files/temps_today.csv"):
        data = pandas.read_csv("Files/temps_today.csv")
        print(data.mean())
    else:
        print("File does not exist! Please make file and try again")
    
    time.sleep(10)



### NOTETOSELF : when i was making this script i came across an error from pandas, this was due to my script initially being called 'pandas'
# so when i type 'import pandas' it was just importing my script and not the third party module pandas.
