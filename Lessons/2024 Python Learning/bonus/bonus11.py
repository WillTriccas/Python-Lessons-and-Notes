#Program to get values from a text file and print the average

def get_average():
    with open("../files/data.txt","r") as file:
        data = file.readlines()

    values = data[1:] #we did this because we dont want to return the temperatures string from the file (which is the title)
    values = [float(i) for i in values]

    average = sum(values) / len(values)
    return average


overall_average = get_average()
print(overall_average)