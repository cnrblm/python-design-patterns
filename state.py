"""
Alt sınıflardan oluşan durum makinalarının davranışı değiştirmesi için kullanılır.
"""
from abc import ABC,abstractmethod

class ComputerState():
    __state=None
    

    def changeState(self,state):
        self.__state=state
        print("new State:",self.__state)

    def getState(self):
        print(self.__state)

class On(ComputerState):

    def __init__(self):
        self.changeState("On")

class Off(ComputerState):

    def __init__(self):
        self.changeState("Off")

class Computer():

    def switchState(self,state):
        self.state=state

def main():
    comp = Computer()
    comp.switchState(On())    
    comp.switchState(Off())   
    comp.state.getState()

if __name__ == "__main__":
    main()

