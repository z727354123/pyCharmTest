#  _*_ encoding=utf-8 _*__*_ encoding=utf-8 _*_
# 元组
class A:
    _name = "A"
    @classmethod
    def printName(self):
        print(self._name)
class B:
    _name = "B"
class StartA(A, B):
    pass
class StartB(B, A):
    pass

print(StartA._name)
print(StartB._name)
StartA.printName()
StartB.printName()

print(A.__dict__)



class B:
    _name = "B"
class BSon(B):
    pass

print(B.__dict__)
print(BSon.__dict__)

print(BSon.__weakref__ is B.__weakref__)