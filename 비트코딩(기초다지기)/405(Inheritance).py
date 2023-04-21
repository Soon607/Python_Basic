class A:
    def __init__(self,a):
        self.attribute1=a
        print('A')
        
class B(A):
    def __init__(self,a,b):
        A.__init__(self,a)
        self.attribute2=b
        print('B')
        
kiki=B(1,2)