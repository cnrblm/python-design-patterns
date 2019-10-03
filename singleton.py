"""
Sürekli nesne üretip kullanmak yerine
tek bir nesne üretip işlemleri onun
üzerinden gerçekleştirmek.
"""
class singleton:
    __instance=None

    @staticmethod
    def getInstance():
        if singleton.__instance==None:
            singleton()
        
        return singleton. __instance
    
    def __init__(self):
        singleton. __instance=self

if __name__ == "__main__":
    s = singleton.getInstance()
    s2 = singleton.getInstance()
    print(s)
    print(s2)