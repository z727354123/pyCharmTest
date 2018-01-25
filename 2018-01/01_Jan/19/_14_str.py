# __str__ 方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "repr姓名:%s, 年龄:%s"%(self.name, str(self.age))
    def __str__(self):
        return "str姓名:%s, 年龄:%s"%(self.name, str(self.age))

p1 = Person('张三', 18)
p2 = Person('李四', 28)

print(p1)

str2 = str(p2)
print(str2, type(str2))



