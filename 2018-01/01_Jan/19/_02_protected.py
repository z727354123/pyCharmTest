# 定义 类公有属性
class Animal:
    _nameA = "AnimalName"
    def test(self):
        print("A " + self._nameA)
        print("A " + Animal._nameA)
class Dog(Animal):
    def test(self):
        print("D " + self._nameA)
        print("D " + self._nameA)

# 测试代码
a = Animal()
a.test()

d = Dog()
d.test()


print("OA " + Animal._nameA)
print("OA " + a._nameA)
print("OD " + Dog._nameA)
print("OD " + d._nameA)
name = "module name"
_name = "module _name"