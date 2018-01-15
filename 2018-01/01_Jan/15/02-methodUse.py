class Person:
    name = "lisi"
    def func1(self):
        print('这是一个 实例方法', self.age, self.name)
        return self
    @classmethod
    def func2(cls):
        print(cls.__bases__[0].name)


p1 = Person()
p1.age = 111


funcX = p1.func1
# funcX()
class Person2(Person):
    name = "XXXXX"
    pass

p2 = Person2()
p2.age = 222
p2.func1()
Person2.func2()
