# 定义一个 生成器
# 生成器 表达式
listA = [str(i)+str(a) for i in range(0, 2) for a in range(3, 5) if (a + i)%2 == 0]
iterA = (i for i in range(0, 200))

print(listA, type(listA))
print(iterA, type(iterA))

print(next(iterA))
print(next(iterA))
# print(next(iterA))
# StopIteration

iterB = iterA.__iter__()

print(next(iterB))
print(next(iterA))
print(iterA.__next__())
print(iterB.__next__())

print(iterA == iterB)
