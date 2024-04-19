
while True:
    username = input("Enter Username (Must be more than 8 Characters): ")
    if len(username) > 8:
        break
    else:
        print('Username too short, please try again')
        continue
    