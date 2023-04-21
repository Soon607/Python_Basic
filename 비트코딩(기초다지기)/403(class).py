# 클래스 작성
class Student:
    def __init__(self,name,math,physics,coding):
        self.name=name
        self.math=math
        self.physics=physics
        self.coding=coding
        
    def average(self):
        average=(self.math+self.physics+self.coding)/3
        return average

def classAverage(array):
    sum=0
    for i in array:
        sum+=i.average()
    return (sum/len(array))

    
JS=Student('Jisso',94,93,83)
HS=Student('Haesung',78,61,93)
MS=Student('Minsoo',100,89,98)
HL=Student('Haeryn',93,87,88)
WJ=Student('Woojin',82,90,84)
JH=Student('Jihyun',88,93,95)

students=[JS,HS,MS,HL,WJ,JH]
print(students)
print(classAverage(students))