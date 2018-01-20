# 定义 类公有属性
class Animal:
    __slots__ = ["name", 'book', '_age']
    ss = 'xxs'
    __nameA = " AnimalName"
    def __init__(self):
        self.book = 'Im book'
    def test(self):
        print("A " + self.__nameA)
        print("A " + Animal.__nameA)
class Dog(Animal):
    def test(self):
        print("D " + self.__nameA)
        print("D " + Dog.__nameA)

# 测试代码
a = Animal()
a.test()
a.name =123
a._age = 123123
# a.name = 'adfsdf'
# print(a.__dict__)

print(a.book)
print(a._age)
# print(a.__dict__)
# print(a.__dict__)
print(Animal.__dict__)
# Animal._Animal__age = 123
# print(a._Animal__age)
# a._Animal__age = 123
# d = Dog()
# d.test()
# AttributeError: 'Dog' object has no attribute '_Dog__nameA'

# AttributeError: type object 'Animal' has no attribute '__nameA'
# print("OA " + Animal._Animal__nameA)
# print("OA " + a.__nameA)
# print("OD " + Dog.__nameA)
# print("OD " + d.__nameA)
name = "module name"
__name = "module _name"
# __all__ = ["__name"]