myList = [1, 2, 3, 4]
myTuple = ('1', '2', '3')
myList.append(998)
# print(myList)   # [1, 2, 3, 4, 998]
myList.extend(myTuple)  # 可以 extend 元组
# print(myList)   # [1, 2, 3, 4, 998, '1', '2', '3']
myList.extend(range(5, 11))
# print(myList)   # [1, 2, 3, 4, 998, '1', '2', '3', 5, 6, 7, 8, 9, 10]

# 乘法运算
listA = [1, 2, 3, 4]
tupleA = ('1', '2', '3')
print(listA * 2)    # [1, 2, 3, 4, 1, 2, 3, 4]
print(listA)        # [1, 2, 3, 4]
print(tupleA * 2)   # ('1', '2', '3', '1', '2', '3')
print(tupleA)       # ('1', '2', '3')
# 加法运算
# print(listA + tupleA) 报错
print(listA + listA)    # [1, 2, 3, 4, 1, 2, 3, 4]
print(tupleA + tupleA)    # ('1', '2', '3', '1', '2', '3')
