# Practicing Inheritance
from abc import *

class A(metaclass=ABCMeta):
    @abstractmethod
    def fun1(self):
        pass
    
class B(A):
    def __init__(self,num):
        self.num=num
    def fun1(self):
        print(self.num)
        
