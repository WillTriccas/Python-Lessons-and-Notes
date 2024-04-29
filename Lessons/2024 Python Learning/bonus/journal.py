date = input("What is todays date? ")
mood = input("How was your day out of 10? ")
thoughts = input("Highlight some of the key events from today: ")

with open(f"../Journal/{date}.txt", "w") as file:
    file.write(mood +"/10" + 2*'\n')
    file.write(thoughts)
