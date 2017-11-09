# 根据 元素遍历
listA = range(1, 11)
listA = listA[::-1]
print(listA)    # range(10, 0, -1)
for item in listA:
    print(listA.index(item), end='=')
    print(item, end=',')
# 0=10,1=9,2=8,3=7,4=6,5=5,6=4,7=3,8=2,9=1,
print()

listA = [1, 2, 1, 3]
for item in listA:
    print(listA.index(item), end='=')
    print(item, end=',')
# 0=1,1=2,0=1,3=3,
# 故 这样遍历， 获取 index 有缺陷
print()
# 修复
listA = [1, 2, 1, 3]
currentIndex = 0
for item in listA:
    print(listA.index(item, currentIndex), end='=')
    print(item, end=',')
    currentIndex += 1
# 0=1,1=2,2=1,3=3,
print()

# 根据索引 遍历
listA = [1, 2, 1, 3]
for index in range(len(listA)):
    item = listA[index]
    print(index, end='=')
    print(item, end=',')
# 0=1,1=2,2=1,3=3,


