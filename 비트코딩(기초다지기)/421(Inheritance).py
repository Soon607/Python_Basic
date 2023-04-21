class Car:
    def __init__(self,minV,maxV):
        self.minV=minV
        self.maxV=maxV

class SportCar(Car):
    def __init__(self,minV,maxV,Zto100):
        Car.__init__(self,minV,maxV)
        self.Zto100=Zto100