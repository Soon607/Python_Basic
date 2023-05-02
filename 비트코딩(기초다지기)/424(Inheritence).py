class Customer:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def withdraw(self,amount):
        if (amount+100)>self.balance:
            print('Not available')
        else:
            self.balance-=(amount+100)
            print(self.name,self.balance)
            
    def deposit(self,amount):
        self.balance+=amount
        print(self.name,self.balance)
        
class VIP(Customer):
    def __init__(self,name,balance):
        Customer.__init__(self,name,balance)
    
    def withdraw(self,amount):
        if amount>self.balance:
            print('Not Available')
        else:
            self.balance-=amount
            print(self.name,self.balance)
            
    def deposit(self,amount):
        self.balance+=(amount*1.005)
        print(self.name,self.balance)
        

class Student(Customer):
    def __init__(self,name,balance,minimum_balance):
        Customer.__init__(self,name,balance)
        self.minimum_balance=minimum_balance
        
    def withdraw(self,amount):
        if (amount)>self.balance:
            print('Not Available')
        elif self.balance-amount<self.minimum_balance:
            print('Not Available')
        else:
            self.balance-=amount
            print(self.name,self.balance)