# 클래스 생성
class Person:
  workingStatus=0
  Atime='0900'
  workHour=8
  
  def __init__(self,name,workingFor,Atime,workHour):
      self.name=name
      self.workingFor=workingFor
      self.Atime=Atime
      self.workHour=workHour
      
def isWorking(p,t):
    at=p.Atime
    wH=p.workHour
    if int(t) in range(int(at),int(at)+wH*100):
        p.workingStatus=1
    else:
        p.workingStatus=0
    return p.workingStatus

a=Person('A','HQ','0900',8)
print(a.name,a.workingStatus)
isWorking(a,'1100')
print(a.name,a.workingStatus)
