# 定义 类公有属性
class Animal:
    nameA = "AnimalName"
    def test(self):
        print("A " + self.nameA)
        print("A " + Animal.nameA)
class Dog(Animal):
    def test(self):
        print("D " + self.nameA)
        print("D " + self.nameA)

# 测试代码
a = Animal()
a.test()

d = Dog()
d.test()

print("OA " + Animal.nameA)
print("OA " + a.nameA)
print("OD " + Dog.nameA)
print("OD " + d.nameA)