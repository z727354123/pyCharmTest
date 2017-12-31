listA = []


def get_num(numA):
    strA = str(numA)
    res = 0
    for i in strA:
        itemNum = int(i)
        res += itemNum ** 3
    return res


for num in range(100, 999):
    if num == get_num(num):
        listA.append(num)
print(listA)
