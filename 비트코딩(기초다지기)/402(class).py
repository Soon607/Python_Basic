class Student:
    def __init__(self,name,age):
        self.university='SNU'
        self.name=name
        self.age=age
        self.isStudying=True
        self.studyHour=0
        
    def study(self):
        if self.isStudying:
            self.studyHour+=1
        
    def hourofstudy(self):
        print('{} 현재 공부 시간:{} 시간'\
            .format(self.name,self.studyHour))
        
    def __str__(self):
        sentence='이름:{}, 나이:{}, 학교:{}, 공부시간:{}'.format(self.name,self.age,self.university,self.studyHour)
        return sentence
        
student1=Student('Jane',23)
student1.study()
student1.study()
print(student1)