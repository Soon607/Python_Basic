# practice
import random
class Character:
    def __init__(self,nickname,Hp,Mp,ST,DX,IQ,LX):
        self.nickname=nickname
        self.Hp=Hp
        self.Mp=Mp
        self.ST=ST
        self.DX=DX
        self.IQ=IQ
        self.LX=LX
    
    def acc(self):
        acc=random.randint(5,10)/10+0.01*self.LX
        return acc
    
    def attack(self,character):
        character.Hp-=(self.ST+self.DX+self.IQ)*self.acc()
    
    def status(self):
        if self.Hp<0:
            print('{}의 HP {}, Mp {}: DIE'.format(self.nickname,self.Hp,self.Mp))
        else:
            print('{}의 HP {} MP {}'.format(self.nickname,self.Hp,self.Mp))
            
            
class Warrior(Character):    
    def attack(self,character):
        character.Hp-=(4*self.ST+self.DX+self.IQ)*self.acc()
        
    def skill(self,character):
        if self.Mp>=10:
            character.Hp-=(8*self.ST*self.acc())
            self.Mp-=10
        else:
            print('No Mp')

class Archer(Character):
    def acc(self):
        acc=random.randint(7,10)/10+0.1*self.LX
        return acc
    
    def attack(self,character):
        character.Hp-=(self.ST+2*self.DX+self.IQ)*self.acc()
        
    def skill(self,character):
        if self.Mp>=30:
            character.Hp-=(self.DX*4)*self.acc()
            self.Mp-=30
            
        else:
            print('No Mp')

            
class Wizard(Character):
    def acc(self):
        acc=random.randint(3,10)/10+0.3*self.LX
        return acc
    
    def attack(self,character):
        character.Hp-=(2*self.DX+4*self.IQ)*self.acc()
        
    def skill(self,character):
        if self.Mp>=50:
            character.Hp-=(10*self.IQ*self.acc())
            self.Mp-=50
            
        else:
            print('No Mp')