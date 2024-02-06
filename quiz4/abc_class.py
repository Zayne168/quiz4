from abc import ABC , abstractmethod
import os

class MyClass(ABC):

    @abstractmethod
    def addData(self,data):
        pass

    @abstractmethod
    def subData(self,data):
        pass

class   SimpleMath(MyClass):    #this class + or - data onto self and overwrites self with that data.
    def __init__(self,number):
        self.number=number
    def addData(self,data):
        self.number=self.number+data
        return self
    def subData(self,data):
        self.number=self.number-data
        return self
class   AdjustOne(MyClass):     #This replaces whatever self is wanted with the data + or - 1 depending on the method used.
    def __init__(self,number):
        self.number=number
    def addData(self,data):
        self.number=data+1
        return self
    def subData(self,data):
        self.number=data-1
        return self

#test material
data=3.1
myO=SimpleMath(3)
myO=myO.addData(data)
myO=myO.subData(2.2)
print(myO.number)
#test material
