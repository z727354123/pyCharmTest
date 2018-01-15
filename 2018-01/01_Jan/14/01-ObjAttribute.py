# 定义一个类
class Person:
    pass
person = Person()

person.name = "张三"
dictA = person.__dict__
dictA['name'] = "xxx"

person.age = 18
dictB = person.__dict__
a = person
print(dictA, type(dictA))
print(dictB, dictA is dictB)
print(person.name)

del person.name
del person.name
del person.age

print(a.__dict__ is dictA)