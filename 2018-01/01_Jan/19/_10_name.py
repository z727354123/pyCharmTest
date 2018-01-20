# name
class Person:
    pass

print(Person.__name__)

Person.__name__ = "XXX"
print(Person.__name__)
# 可以修改 __name__，但是 无法直接修改直接打印类，打印出来的名字
XXX = Person
print(XXX)
print(Person.__dict__)


