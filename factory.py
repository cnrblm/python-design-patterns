"""
Birbirine benzer sınıfların tek bir factory
sınıfı üzerinden üretilmesi
"""
class person:    
    name="person"
    def get_name(self):
        return self.name

class manager(person):
    name="manager"

class personFactory:
    def create_person(self,cls):
        return cls()

p = personFactory().create_person(person).get_name()
print(p)
m = personFactory().create_person(manager).get_name()
print(m)