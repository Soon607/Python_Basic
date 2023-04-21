class A:
    def greeting(self):
        print('안녕하세요 A 입니다.')
        
class B(A):
    def greeting(self):
        print('안녕하세요 B 입니다.')

class C(B):
    pass

x=C()
x.greeting()
y=B()
y.greeting()