class Student:
    def __init__(self,name,age,school):
        self.name=name
        self.age=age
        self.school=school
        
class Undergraduate:
    def __init__(self,name,age,school,grade):
        Student.__init__(self,name,age,school)
        self.grade=grade
        
    def aboutMe(self):
        print(self.name,self.age,self.school,self.grade)
    
info=Undergraduate('Jude',19,'Liverpool',100)
info.aboutMe()