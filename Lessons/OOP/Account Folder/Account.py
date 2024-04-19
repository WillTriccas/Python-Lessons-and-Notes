class Account:
    
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as myfile:
            self.balance = int(myfile.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount

# ATM, if we were to execute withdraw and deposit and print the self.balance, it would show us what it had done, but it would not commit those changes to 
# the file, therefore we have to make a commit function to do this

    def commit(self):
        with open(self.filepath, 'w') as myfile:
            myfile.write(str(self.balance))

#NTS: YOU CANT EXECUTE OUR COMMIT FUNCTION IF WE HAVENT ACTUALLY MADE ANY CHANGES TO THE SELF.BALANCE ATTRIBUTE

#Below is a class made using inheritance:

class Checking(Account):

    def __init__(self, filepath):
        Account.__init__(self,filepath)

    def transfer(self, amount):
        self.fee = 1
        self.balance = self.balance - amount - self.fee

checking = Checking("Lessons/OOP/Account Folder/balance.txt")

checking.transfer(400)
checking.commit()
print(checking.balance)






