class Person:
    def __init__(self):
        self.count = 0
    def __getitem__(self, key):
        self.count += 1
        print('key =', key, end=', ')
        if self.count == 10:
            # raise StopAsyncIteration("停止")
            # StopAsyncIteration: 停止
            raise StopIteration("结束了")
        return self.count


p1 = Person()

# for i in p1:
#     print('value = ' ,i)
    # p1.count = 10

class Son1:
    def __iter__(self):
        print('__iter__ ', end=", ")
        return [1, 2, 3].__iter__()
    def __getitem__(self, key):
        return 2;


s1 = Son1()
for i in s1:
    print(i, end=", ")



class Son2:
    def __init__(self):
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.count += 1
        print('\n', '__next__',  end=',')
        if self.count >= 5:
            raise StopIteration()
        return  self.count



s2 = Son2()
for i in s2:
    print(i, end=", ")

s2.count = -2
for i in s2:
    print(i, end=", ")









