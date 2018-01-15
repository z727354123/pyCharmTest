# 2. 删除操作
class Animal:
    name = "动物"
    age = 10

# a1 = Animal()
# print(Animal.name)
# # 动物
# del a1.__class__.name
# print(Animal.__dict__)
# {'__module__': '__main__',
# 'age': 10, '__dict__': <attribute '__dict__' of 'Animal' objects>,
# '__weakref__': <attribute '__weakref__' of 'Animal' objects>,
# '__doc__': None}

#  修改类 __dict__
dictA = Animal.__dict__
print(dictA)
dictA['name'] =" xxx"
# TypeError: 'mappingproxy' object does not support item assignment



# print(Animal.name)

# # 1. 定义类
# class Person:
#     name = "人类"
# # 获取 dict
# print(Person.__dict__)
# # {'__module__': '__main__',
# # 'name': '人类',
# # '__dict__': <attribute '__dict__' of 'Person' objects>,
# # '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# # '__doc__': None}
# print(Person) # <class '__main__.Person'>
# print(Person.__class__) # <class 'type'>
# print(Person is Person.__class__) # False
# print(type(Person.__class__))# <class 'type'>
# print(type(Person)) # <class 'type'>
# print(Person.__class__ is type(Person)) # True
# print(Person.__class__ is type(Person.__class__)) # True
# print(Person.__class__ is Person.__class__.__class__) # True
# # 类似 原型链
# p1 = Person()
# p2 = Person()
# p1.name = "xx"
#
# Person.name = "age"
#
# print(p1.name)
# print(p2.name)
# print(Person.name)
#
# # 设置 不存在的属性
# Person.age = 123
# print(p2.age)
#
# print(type(p1))
#
#
# # 查询操作
#
# dictA = Person.__dict__
# print(dictA)
# Person.sex = "boy"
# print(dictA)
# class Nxx(Person):
#     typex = 999
#
#
# p2.__class__ = Nxx
# print(p2.typex)