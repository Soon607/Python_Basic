# 조건을 만족하는 Triangle 클래스 작성하기
# 1. Triangle 클래스는 세 변의 길이 a,b,c,를 속성으로 가지면, 생성자(__init__)를 통해 세변의 길이를 입력받는다.
# 2. area() 메서드를 통해 Triangle 객체의 넓이를 반환한다.
# 3. get() 메서드를 호출하여 삼각형이 정삼각형,직각삼각형인지에 대한 정보를 얻을 수 있다.
import math

class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(self.a+self.b+self.c)/2
        area2=s*(s-self.a)*(s-self.b)*(s-self.c)
        return math.sqrt(area2)
        
    def get(self):
        A=self.a**2
        B=self.b**2
        C=self.c**2
        if A==B and A==C:
            return '정삼각형'
        elif A+B==C or A+C==B or B+C==A:
            return '직각삼각형'
        else:
            return '일반 삼각형'
        
T1=Triangle(4,5,6)
print(T1.area(),T1.get())