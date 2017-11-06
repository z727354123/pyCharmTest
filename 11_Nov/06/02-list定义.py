# _*_ encoding:utf-8 _*_
# 列表生成式
# myList = range(10)
# print(myList)
# myList = range(1, 11)
# print(myList)

# 列表推导式
# myList = [1, 2, 3, 4, 5]
# # 原始方式
# newList = []
# for item in myList:
#     if item % 2 == 0:
#         continue
#     newList.append(item ** 2)
#
# print newList   # [1, 9, 25]
# # 新方式
# print [item for item in myList]
# # [1, 2, 3, 4, 5]
# print [item ** 2 for item in myList]
# # [1, 4, 9, 16, 25]
# print [item ** 2 for item in myList if item % 2 != 0]
# # [1, 9, 25]

listA = ['1', '2', '3']
listB = ['a', 'b', 'c']
print [itemA + itemB for itemA in listA for itemB in listB]
