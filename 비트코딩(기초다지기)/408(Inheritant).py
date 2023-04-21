class A:
    def __init__(self,a):
        self.valueA=a
        
class B(A):
    def __init__(self,a,b):
        A.__init__(self,a)
        self.valueB=b
        
class C(B):
    def __init__(self,a,b,c):
        B.__init__(self,a,b)
        self.valueC=c
        
obj_B=B(1,3)
obj_C=C(2,4,6)
print(obj_B.valueA,obj_B.valueB)
print(obj_C.valueA,obj_C.valueB,obj_C.valueC)