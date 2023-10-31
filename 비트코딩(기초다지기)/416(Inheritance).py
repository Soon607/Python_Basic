# Practicing Inheritance

class A:
    def __init__(self,a,b):
        self.A=a
        self.B=b
        print(self.A+self.B)
        
class B:
    def __init__(self,a,b,c):
        A.__init__(self,a,b)
        self.C=c
        print(self.A+self.B+self.C)
        
obj_A=A(3,6)
obj_B=B(2,4,8)