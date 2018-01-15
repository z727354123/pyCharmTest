# 定义 实例 / 类 / 静态 方法

class Person:

    name = "lisi"
    def func1(self):
        print('这是一个 实例方法')
        return self

    @staticmethod
    def func3():
        print('这是一个 静态方法')

    @classmethod  # 也是一个 装饰器
    def func2(cls):
        print('这是一个 类方法')
        return cls




p1 = Person()
p2 = Person()

print(Person.func1(p1) == p1)
print(p1.func1() == p1)

print(p1.func2() == Person)
print(Person.func2() == Person)

print(p1.func3())
print(Person.func3())

print(p1.func1 is Person.func1)     # False
print(p1.func2 is Person.func2)     # False
print(p1.func2 == Person.func2)     # True
print(p1.func3 is Person.func3)     # Ture

# print(p1.func2(1) == Person)
# print(Person.func2(1) == Person)
# TypeError: func2() takes 1 positional argument but 2 were given

def fun4(self):
    print("xxx")
    print(self)

p1.func4 = fun4

p1.func4(p1)
print(p1.__dict__)