#클래스 기초

class Student():
    def __init__(self):
        self.age='20 years old'
        self.height='170cm'
        
student1=Student(); student2=Student()
print(student1.age,student1.height)
print(student2.age,student2.height)

student1.name='Woori'
student1.height='159cm'
student2.name='Minho'
student2.height='182cm'

print(student1.name,student1.age,student1.height)
print(student2.name,student2.age,student2.height)