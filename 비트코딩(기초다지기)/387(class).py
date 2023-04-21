# 이름 속성과 자신의 이름을 출력하는 info()메소드를 가진 Student클래스를 정의한 프로그램
class Student:
    name='Dohee'  #attribute
    def info(self): # method
        print('My name is',self.name)
        
s=Student()
s.info()
s.name='Hongjun'
s.info()