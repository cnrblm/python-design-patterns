class Shape():
    
    def draw(self):
      pass

class Rectangle(Shape):
    
    def draw(self):
        print(Rectangle.__name__," draw()")

class Circle(Shape):
    
    def draw(self):
        print(Circle.__name__," draw()")

class ShapeCreator():
    __circle,__rectange=None,None

    def __init__(self):
        self.__circle=Circle()
        self.__rectange=Rectangle()
    
    def drawCircle(self):
        self.__circle.draw()

    def drawRegtangle(self):
        self.__rectange.draw()


def main():
    creator = ShapeCreator()
    creator.drawCircle()
    creator.drawRegtangle()

if __name__ == "__main__":
    main()