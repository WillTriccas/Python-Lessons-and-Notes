def pchecker(password):
    if len(password) < 8:
        return False
    else: 
        return True

print(pchecker('Password123'))
