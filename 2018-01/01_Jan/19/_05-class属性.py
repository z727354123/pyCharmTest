# _*_ encoding=utf-8 _*_
class Animal:
    name = 'Animal'

class Dog(Animal, object):
    name = 'Dog'

print(Dog.name)
print(Dog.__bases__)
print(Animal.__bases__)
# py2 默认 不继承 object