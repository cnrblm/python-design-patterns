from abc import ABC,abstractmethod

class Iterator(ABC):

    @abstractmethod
    def hasnext(self):
        pass
    @abstractmethod
    def next(self):
        pass

class Container(ABC):

    @abstractmethod
    def getIterator(self):
        pass


class NameIterator(Iterator):
    __index=-1
    def __init__(self,names):
        self.names=names

    def hasnext(self):
        if self.__index<len(self.names)-1:
            return True
        else:
            return False

    def next(self):
        if self.hasnext():
            self.__index+=1
            return self.names[self.__index]


class Names(Container):
    names=["ali","veli"]

    def getIterator(self):
        return NameIterator(self.names)

def main():
    nameRepo = Names()
    nameiter=nameRepo.getIterator()
    while(nameiter.hasnext()):
        print(nameiter.next())



if __name__ == "__main__":
    main()
