# class 선언
class Square:
    h=10
    v=20
    def __init__(self,h,v):
        self.h=h
        self.v=v
        
    def area(self):
        return self.h*self.v

s=Square(5,10)
a=s.area()
print(a)
