class Person1:
    # __slots__ = ['age', 'name']
    # ValueError: 'name' in __slots__ conflicts with class variable
    __slots__ = ['age']
    name = "lisi"
class Person2:
    name = "张三"
    __slots__ = ['age']

p1 = Person1()
p2 = Person2()

p1.age = 123
p2.age = 321
# p1.name = "xx"
# AttributeError: 'Person1' object
# attribute 'name' is read-only