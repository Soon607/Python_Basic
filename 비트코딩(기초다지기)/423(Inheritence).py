# class practice
class Customer:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def withdraw(self,amount):
        if amount+100>self.balance:
            print('Not available')
        else:
            self.balance-=(amount+100)
        
    def deposit(self,amount):
        self.balance+=amount
        print(self.name,self.balance)