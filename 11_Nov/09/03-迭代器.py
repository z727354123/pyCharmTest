import collections
# 判定是否是 可迭代对象
boolA = False
numA = 998
# True
# print(isinstance([], collections.Iterable))
# print(isinstance('', collections.Iterable))
# # False
# print(isinstance(boolA, collections.Iterable))
# print(isinstance(numA, collections.Iterable))

# 判定是否是 迭代器
# obj = ['a', 'b', 'c', 'd']
# iterObj = iter(obj)
# print(obj)          # ['a', 'b', 'c', 'd']
# print(iterObj)      # <list_iterator object at 0x101a5c908>
# print(isinstance(iterObj, collections.Iterator))    # True
# print(isinstance(obj, collections.Iterator))        # False
#
# print(isinstance(iterObj, collections.Iterable))    # True
# print(isinstance(obj, collections.Iterable))        # True

# # for in 迭代器
# obj = ['a', 'b', 'c', 'd']
# iterObj = iter(obj)
# for item in iterObj:
#     print(item, end=', ')
#     # a, b, c, d,
# for item in iterObj:
#     print(item, end=', ')
#     # 没有进到这个 for
# for item in obj:
#     print(item, end=', ')
#     # a, b, c, d,
# for item in obj:
#     print(item, end=', ')
#     # a, b, c, d,

# next() 函数遍历迭代器
obj = ['a', 'b', 'c', 'd']
it = iter(obj)

for v in it:
    print(v)
    for i in it:
        print(v, i)
# a
# a b
# a c 
# a d

# for i in range(4):
#     print(i, next(it), end=', ')
#     # 0 a, 1 b, 2 c, 3 d,

# next(it)
# Traceback (most recent call last):
#   File "/Users/Fizz_kai/Documents/workspace/Python/11_Nov/09/03-迭代器.py", line 45, in <module>
#     next(it)
# StopIteration
