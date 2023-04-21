# __init__(객체생성) __del__(소멸자)

class Student:
    name='student'
    age=0
    def __init__(self,name,age):
        print('객체초기화')
        self.name=name
        self.age=age
    
    def __del__(self):
        print('객체삭제')
        
    def info(self):
        print('My name is',self.name)
        print("I'm",self.age,'years old')
        
s=Student('Jaehyun',22)
s.info()
del s
print(type(s))