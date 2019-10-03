"""
Factory bir gruba yönelik çalışırken,
Abstract factory birden fazla gruba yönelik
çalışır.
"""
class CarFactory:
    name=None
    model=None
    def get_model(self):
        return self.model
    def get_name(self):
        return self.name

class MercedesFactory(CarFactory):
    name="mercedes"
    model="2019"

class AudiFactory(CarFactory):
    name="Audi"
    model="2019"

class Cars:
    def create_Car(self,cls):
        return cls

if __name__ == "__main__":
    audi = AudiFactory()
    mercedes=MercedesFactory()
    name = Cars().create_Car(audi).get_name()
    print(name)
