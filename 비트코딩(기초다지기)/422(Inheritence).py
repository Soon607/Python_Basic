# class
class Car:
    distance=0
    def __init__(self,minV,maxV):
        self.minV=minV
        self.maxV=maxV
        
    def drive(self):
        self.distance+=self.maxV*0.5
    
class SportCar(Car):
    def __init__(self,minV,maxV,rush):
        Car.__init__(self,minV,maxV)
        self.rush=rush
        
    def drive(self):
        if self.rush==1:
            self.distance+=self.maxV*0.8
        else:
            self.distance+=self.minV*0.5
    