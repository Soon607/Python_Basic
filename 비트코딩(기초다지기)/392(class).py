# 클래스 기초

class Student():
    def __init__(self,name,age):
        self.university='SNU'
        self.name=name
        self.age=age
        self.isStudying=True
        self.StudyHour=0
        
    def study(self):
        if self.isStudying:
            self.StudyHour+=1
            
    def hourofstudy(self):
        print('{} 현재 공부시간:{} 시간'\
            .format(self.name,self.StudyHour))
        
student1=Student('Jane',23)
student2=Student('Dohee',21)
student1.isStudying=False

student1.study()
student1.study()
student2.study()
student1.hourofstudy()
student2.hourofstudy()