# _*_ encoding=UTF-8 _*_
class Person(object):
    # __slots__ = []      # 这里不需要写 age
    __age = 18
    # 我是 属性装饰器
    @property
    def age(self):
        return self.__age
    @age.deleter
    def age(self):
        print("delete")
    @age.setter
    def age(self, value):
        print('setter')
        self.__age = value



p = Person()
print(p.age)
p.age = 123
print(p.age)




print(Person.__bases__)
p.age = 34


