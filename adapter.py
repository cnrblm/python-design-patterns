"""
Bir nesne için çağrıları yakalar ve bunları ikinci nesne tarafından tanınabilen format ve arabirime dönüştürür.
adapte eder.
"""

class Car():

    def hello(self):
        print("old car")

class NewCar():

    def new_hello(self):
        print("new car")

class Adapter(Car):

    def __init__(self,newcar):
        self.newcar = newcar
    
    def hello(self):
        self.newcar.new_hello()


def main():
    car = Car()
    car.hello()

    ncar = NewCar()
    adapter = Adapter(ncar)
    adapter.hello()

if __name__ == "__main__":
    main()



