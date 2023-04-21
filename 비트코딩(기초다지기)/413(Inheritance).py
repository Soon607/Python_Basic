class A:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        return (self.num1+self.num2)
    
class B(A):
    def __init__(self,num1,num2,num3):
        A.__init__(self,num1,num2)
        self.num3=num3
    def sum(self):
        return (self.num1+self.num2+self.num3)
