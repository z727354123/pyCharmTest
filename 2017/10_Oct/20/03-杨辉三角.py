line = 1;   # 定义长度

# 求和
def getSum (listA, index):
    if index == 0:
        return 1
    if index == len(listA):
        return 1
    return listA[index - 1] + listA[index]


# 调用方法 返回 数组
def getList (line):
    listA = []
    for lineNum in range(line):
        listSon = []
        if lineNum == 0:
            listSon.append(1)
        else:
            for i in range(lineNum + 1):
                listSon.append(getSum(listA[lineNum - 1], i))
        listA.append(listSon)
    return listA
# 打印 数组
def printList (listA):
    for i in listA:
        print(i)

listA = getList(18)
printList(listA)
# print(listA)