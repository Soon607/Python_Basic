class A:
    def fun1(self):
        print('A')
        
class B(A):
    def fun2(self):
        super().fun1()
        print('B')
        
b=B()
b.fun2()
