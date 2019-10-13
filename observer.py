"""
Bir sınıfta değişiklik olduğunda diğer sınıflarda bu değişikliklerin 
haberdar olması amaçlı kullanılan pattern. 

"""
class Observer():
    def __init__(self,subject):
        self.subject = subject
    
    def update(self):
        pass

class DownloadObserver(Observer):
    def __init__(self,subject):
        super().__init__(subject)
        subject.attach(self)
    
    def update(self):
        print("Subject changed: ",self.subject.getState())
    
class Subject():
    observers=[]
    state=None

    def attach(self,o):
        self.observers.append(o)
    
    def getState(self):
        return self.state
    
    def setState(self,s):
        self.state=s
        self.notifyAllObservers()
    
    def notifyAllObservers(self):
        for i in self.observers:
            i.update()
    
def main():
    subject=Subject()
    DownloadObserver(subject)
    subject.setState(1)


if __name__ == "__main__":
    main()


