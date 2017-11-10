import collections
# 判定是否是 可迭代对象
boolA = False
numA = 998
# True
print(isinstance([], collections.Iterable))
print(isinstance('', collections.Iterable))
# False
print(isinstance(boolA, collections.Iterable))
print(isinstance(numA, collections.Iterable))
