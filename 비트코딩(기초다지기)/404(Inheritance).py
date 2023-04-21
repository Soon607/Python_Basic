class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('name:{}, age{}'.format(self.name,self.age))
        
class Stdeunt(Person):
    def __init__(self,name,age,school):
        Person.__init__(self,name,age)
        self.school=school
    def goingto(self):
        print('{} is going to {}'.format(self.name,self.school))
        
