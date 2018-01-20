# _*_encoding=utf-8_*_
# setattr
class Person:
    # 当 对象 增/改 属性时，都会调用此方法
    def __setattr__(self, key, value):
        self.__dict__[key] = value
        return

p = Person()

p.age = 12;
print ( p.__dict__)
print (p.age)

