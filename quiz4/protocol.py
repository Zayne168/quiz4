from typing import Protocol
import os

class MyClass(Protocol):

    
    def addData(self,data:float)->float:
        ...
    
    def subData(self,data:float)->float:
        ...

class   SimpleMath(MyClass):    #this class + or - data onto self and overwrites self with that data.
    def __init__(self,number)->None:
        self.number=number
    def addData(self,data)->None:
        self.number=self.number+data
        print(self.number)
    def subData(self,data)->None:
        self.number=self.number-data
        print(self.number)
class   AdjustOne(MyClass):     #This replaces whatever self is with the data + or - 1 depending on the method used.
    def __init__(self,number)->None:
        self.number=number
    def addData(self,data)->None:
        self.number=data+1
        print(self.number)
    def subData(self,data)->None:
        self.number=data-1
        print(self.number)

#test material
data=3.1
myO : MyClass=SimpleMath(3)
myO.addData(data)
myO.subData(2.2)
print(myO.number)
#test material
