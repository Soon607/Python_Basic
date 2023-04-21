class A:
    def a(self):
        return self.b()
    def b(self):
        return 'A'
    
class B(A):
    def b(self):
        return 'B'
    
a=A()
b=B()
print(a.a(),b.a())
print(a.b(),b.b())