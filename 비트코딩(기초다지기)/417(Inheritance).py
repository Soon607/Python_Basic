class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def info(self):
        print('삼각형입니다.')
        
class Equilateral(Triangle):
    def __init__(self,ln):
        Triangle.__init__(self,ln,ln,ln)
        
    def info(self):
        print('정삼각형입니다.')
        
        
a=Equilateral(3)
a.info()