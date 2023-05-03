import random
# class practice
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
    
    def attac(self,character):
        character.Hp-=(self.ST+self.DX+self.IQ)*self.acc()
    
    def status(self):
        if self.Hp<0:
            print('{}의 HP {}, Mp {}: DIE'.format(self.nickname,self.Hp,self.Mp))
        else:
            print('{}의 HP {} MP {}'.format(self.nickname,self.Hp,self.Mp))
            