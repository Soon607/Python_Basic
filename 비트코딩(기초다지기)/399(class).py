# 클래스 작성
import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    
    def get(self):
        return (self.x,self.y)
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def distance(self,p):
        X=self.x-p.x
        Y=self.y-p.y
        return math.sqrt(X**2+Y**2)
    
    
def dist(p1,p2):
    X=p1.x-p2.x
    Y=p1.y-p2.y
    return math.sqrt(X**2+Y**2)

p1=Point(6,7)
p2=Point(2,4)
print(p1.distance(p2))
p2.move(3,3)
print(dist(p1,p2))