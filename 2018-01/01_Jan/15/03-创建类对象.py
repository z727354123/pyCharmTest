# tupleA = ()
def a (self):
    print(self.name)

Person = type("Person", (), {'name':'lisi', 'run':a})

p1 = Person()

p1.run()


def b (str):
    print(str)
    return str

class Person:
    age = b(18)
    name = b("李四")  # 无视一个属性

# 指明元类方式 1
class Dog:
    __metaclass__ = type
    pass
# 指明元类方式 2
class Cat(metaclass=type):
    pass

class Animal:
    pass
# 指明模块 元类
__metaclass__ = type


# 继承写法
class Cat2(Animal):
    name = "cat"

# 类的描述
class Person:
    """
    关于这个类的描述，
    类的作用，类的 构造函数等等，
    类属性的描述；
    """
    name = "person"
    age = 18
    def say(self, something):
        """
        这个方法的作用效果
        :param something: 参数的含义，参数的类型，是否有默认值
        :return: 返回结果的含义，结果的类型
        """
        return something

# 查看
# help(Person)



