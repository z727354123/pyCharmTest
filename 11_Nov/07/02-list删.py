listA = [1, 2, 3, 4]
# del listA
# print(listA) NameError: name 'listA' is not defined
# del listA[1]
# print(listA)    # [1, 3, 4]


# pop() 方法
listA = [1, 2, 3, 4]
# listA.pop(4)    IndexError: pop index out of range
# listA[4] IndexError: list index out of range
# print(listA.pop(), listA, sep=' and ') # 4 and [1, 2, 3]
# print(listA.pop(-1), listA, sep=' and ') # 3 and [1, 2]



# remove() 方法
listA = [1, 2, 3, 4]
# res = listA.remove(8) ValueError: list.remove(x): x not in list
# res = listA.remove(3)
# print(res, listA, sep=' and ')  # None and [1, 2, 4]

# 遍历删除的坑
listA = [1, 2, 2, 4]
for num in listA:
    print(num, end=' and ')  # 1 and 2 and 4 and
    if num == 2:
        listA.remove(num)
print('')
print(listA)    # [1, 2, 4]
