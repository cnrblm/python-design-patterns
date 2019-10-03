"""
Nesne oluştururken verilecek olan parametrelerin
tam olarak kestirelemediği noktalarda kullanılır.
"""
class Human:
    def __init__(self):
        self._name=None
        self._surname=None
        self._age=None
        self.builder=Human.Builder(self)
    
    def show_prop(self):
        print(self._name)
        print(self._surname)
        print(self._age)

    class Builder:

        def __init__(self,top):
            self.top = top

        def name(self,name):
            self.top._name = name
            return self

        def surname(self,surname):
            self.top._surname = surname
            return self

        def age(self,age):
            self.top._age = age
            return self

        def build(self):
            return self.top

if __name__ == "__main__":
    h=Human().builder.name("ahmet").build()
    h.show_prop()