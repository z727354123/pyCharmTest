# # 私有方法
# class Person:
#     def __init__(self):
#         self.__name = "李四1"
#         self._name = "李四2"
#         self.name = "李四3"
#         self.age2 = self.age
#     def age(self):
#         print(self.__name)
#         return self
#
# p = Person()
#
# def test(self):
#     print(self.name)
#     print(self._name)
#     # print(self.__name)
#     # AttributeError: 'Person' object has no attribute '__name'
# Person.test = test
#
# p.test()
#

class Person:
    def __run(self):
        print('__runA')
    def _Person__run(self):
        print('_Person__run')
class BB:
    def _BB__run(self):
        print('_BB__run')
    def __run(self):
        print('__runB')

p = Person()
b = BB()

Person.__dict__['_Person__run'](p)
BB.__dict__['_BB__run'](b)















