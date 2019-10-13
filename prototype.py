import copy

class Shape():
    def __init__(self,shapeid):
        self.shape=shapeid
    
    def clone(self):
      pass

class Rectangle(Shape):
    def __init__(self,shapeid):
        super().__init__(shapeid)
    
    def clone(self):
        return copy.copy(self)

class Circle(Shape):
    def __init__(self,shapeid):
        super().__init__(shapeid)
    
    def clone(self):
        return copy.copy(self)

class ShapeCashe():
    m =dict()
    r1,r2=None,None

    @staticmethod
    def initialize():
        ShapeCashe.__r1 = Rectangle("1")
        ShapeCashe.m["1"]=ShapeCashe.__r1
        ShapeCashe.__r2 = Circle("2")
        ShapeCashe.m["2"]=ShapeCashe.__r2
        
    @staticmethod
    def getShape(shapeid):
        return ShapeCashe.m[shapeid].clone()

def main():
    ShapeCashe.initialize()
    rectange1=ShapeCashe.getShape("1")
    print (rectange1)
    rectange2=ShapeCashe.getShape("1")
    print (rectange2)
    circle1=ShapeCashe.getShape("2")
    print (circle1)
    

if __name__ == "__main__":
    main()