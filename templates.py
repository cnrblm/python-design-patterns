from abc import ABC,abstractmethod

class makeMeal(ABC):

    @abstractmethod
    def prepare(self):
        pass
    @abstractmethod
    def cook(self):
        pass
    
    def eat(self):
        self.prepare()
        self.cook()

class Pizza(makeMeal):

    def prepare(self):
        print("prepare pizza")
    
    def cook(self):
        print("cook pizza")

def main():
    p=Pizza()
    p.eat()

if __name__ == "__main__":
    main()

    