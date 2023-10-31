#클래스 기초
class Student():
    def __init__(self,name,age):
        self.university='SNU'
        self.name=name
        self.age=age
        
s1=Student('Jane',23)
s2=Student('Dohee',21)
print(s1.university,s1.name,s1.age)
print(s2.university,s2.name,s2.age)
