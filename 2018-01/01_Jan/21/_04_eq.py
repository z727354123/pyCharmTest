class Person:
    def __init__(self, age=15):
        self.age = age
    # 默认比较 引用地址
    def __eq__(self, other):
        print('__eq__', self.age, other.age, end=" , ")
        return False
    def __ne__(self, other):
        print('__ne__', self.age, other.age, end=" , ")
        return False

    def __gt__(self, other):
        print('__gt__', self.age, other.age, end=" , ")
        return True
    def __lt__(self, other):
        print('__lt__', self.age, other.age, end=" , ")
        return True
    def __bool__(self):
        return False
    # def __ge__(self, other):
    #     print('__ge__', self.age, other.age, end=" , ")
    #     return True
    def __le__(self, other):
        print('__le__', self.age, other.age, end=" , ")
        return True



# TypeError: '>' not supported between
# instances of 'Person' and 'Person'
p1 = Person()
p2 = Person(16)


print(p1 == p2)
# 没有 __eq__ 就是 not(p1 == p2)
print(p1 != p2)

# 这里不会调用 __gt__ & __eq__
# 只会调用 not __le__
print(p1 >= p2)
print(p1 <= p2)

# print(p1 < p2 > p1)

print(not p1)