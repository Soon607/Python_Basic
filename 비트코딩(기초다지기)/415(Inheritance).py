# Practicng Inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print('bark')
        
class Duck(Animal):
    def speak(self):
        print('quack')
        
a,b,c=Animal('a'),Dog('b'),Duck('c')
a.speak()
b.speak()
c.speak()