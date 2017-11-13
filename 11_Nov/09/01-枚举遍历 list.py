# 枚举函数
listA = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
enum = enumerate(listA)
print(enum)
# <enumerate object at 0x00681BC0>
print(list(enum))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g')]

for item in enum:
    print(item)
    # 不打印 东西！！！
    # 可能 list 转换了一下， enum 就变了
print(enum)
# <enumerate object at 0x005F1C60>


enum = enumerate(listA)
print(enum)
# <enumerate object at 0x005F1CB0>
for item in enum:
    print(item, end='-')
    # (0, 'a')-(1, 'b')-(2, 'c')-(3, 'd')-(4, 'e')-(5, 'f')-(6, 'g')-
print()
print(enum)
# <enumerate object at 0x006F1CB0>


for idx, val in enum:
    print(idx + '=' + val, end=',')
    # 不打印 东西！！！
    # 枚举一次， enum 就变了

for idx, val in enumerate(listA):
    print(str(idx) + '=' + val, end=', ')
    # 0=a, 1=b, 2=c, 3=d, 4=e, 5=f, 6=g,
print()

# index 越界
listA = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for item in enumerate(listA, 9999):
    print(item, end=' - ')
# (9999, 'a') - (10000, 'b') - (10001, 'c') - (10002, 'd') - (10003, 'e') - (10004, 'f') - (10005, 'g') -


