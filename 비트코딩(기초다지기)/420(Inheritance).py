class A:
    n=3
    def a(self):
        self.b()
        self.n+=1
        return self.n
    
    def b(self):
        self.n+=2
        return self.n
    
class B(A):
    n=2
    def b(self):
        self.n+=3
        return self.n
    
a=A()
b=B()
print(a.a(),b.a())
print(a.b(),b.b())