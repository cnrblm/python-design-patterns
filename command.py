"""
Komut Deseni, eylemler arasında bir soyutlama düzeyi ekler ve bu eylemleri çağıran bir nesne içerir.

"""
from abc import ABC,abstractmethod

class Shape():
    color=None

    def redColor(self):
        self.color="red"
        print(self.color)

    def blueColor(self):
        self.color="blue"
        print(self.color)

class ColorPicker(ABC):
    @abstractmethod
    def execute(self):
        pass

class RedColorChanger(ColorPicker):

    def __init__(self,shape):
        self.shape=shape
    
    def execute(self):
        self.shape.redColor()
    
class BlueColorChanger(ColorPicker):

    def __init__(self,shape):
        self.shape=shape
    
    def execute(self):
        self.shape.blueColor()

class Commander():
    com_list=[]

    def addCommand(self,picker):
        self.com_list.append(picker)
    
    def executeCommand(self):
        for i in self.com_list:
            i.execute()
        self.com_list.clear()

def main():
    shape=Shape()
    rshape=RedColorChanger(shape)
    bshape = BlueColorChanger(shape)
    com=Commander()
    com.addCommand(rshape)
    com.addCommand(bshape)
    com.executeCommand()

if __name__ == "__main__":
    main()