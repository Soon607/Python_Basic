# 이름 정보를 저장하는 name 속성과 직장 정보를 저장하는 workingFor 속성을 가진 Person클래스를 작성

class Person:
    def __init__(self,name,workingFor):
        self.name=name
        self.workingFor=workingFor
        
a=Person('k','work')
print(a)
print(a.name)
print(a.workingFor)