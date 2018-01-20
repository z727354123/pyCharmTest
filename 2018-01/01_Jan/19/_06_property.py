# _*_ encodig=utf-8 _*_
class Animal():
    pass
class Person(Animal):

    def __init__(self):
        self.__age = 18
    def set_age(self, value):
        print 'set'
        self.__age = value
    def get_age(self):
        return self.__age
    def del_age(self):
        del self.__age
    age = property(get_age, set_age, del_age, "I'm a 'age' property.")

p = Person()

print(p.age)
print(p.__dict__)
p.age = 123
print(p.age)
print(p.__dict__)

