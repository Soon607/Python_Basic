class A:
    def do(self):
        print('A completed')
        
class B(A):
    def do(self):
        print('B completed')
        super().do()
        
class C(A):
    def do(self):
        print('C Completed')
        super().do()
        
class D(B,C):
    def do(self):
        print('D completed')
        super().do()
        
d=D()
d.do()