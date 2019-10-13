"""
Karmaşıklaşan projelerde alt sınıf oluşturmayı daha hale getirmek için kullanılır.
"""
from  abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
      pass


class Rectangle(Shape):
    
    def draw(self):
        print(Rectangle.__name__," draw()")

class Circle(Shape):
    
    def draw(self):
        print(Circle.__name__," draw()")

class RedShape(Shape):
    decorateShape=None

    def __init__(self,decorateShape):
        self.decorateShape= decorateShape
    
    def draw(self):
        self.decorateShape.draw()
        self.setRedBorder()
    
    def setRedBorder(self):
        print("Border Color Red")

def main():
    r1=Rectangle()
    print("Before")
    r1.draw()
    print("after")
    redr1=RedShape(r1)
    redr1.draw()


if __name__ == "__main__":
    main()