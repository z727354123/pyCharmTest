# # _*_ encoding:utf-8 _*_
# # 获取元素 索引
# listA = [1, 2, 3, 4, 5, 6, 6]
# # print listA.index(1, 1) 找不到报错
# # ValueError: 1 is not in list
# # print listA.index(6)        # 5
# # print listA.index(6, 6)     # 6
#
#
# # 获取 元素出现 次数
# listA = [1, 2, 3, 4, 5, 6, 6, 3, 33]
# print listA.count(3)    # 2
# print listA.count(2)    # 1
# print listA.count(0)    # 0
#
#
# # 切片操作
# listA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print listA[3:9:3]       # [3, 6]
# print listA[3:10:3]      # [3, 6, 9]
# print listA[3:99:3]      # [3, 6, 9]
# print listA[-99:99:3]    # [0, 3, 6, 9]
#
#
# # 特殊操作
# listA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# listB = listA[:]    # 复制数组
# listB.append(110)
# print listA, listB
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 110]
# listB = listA[::-1]     # 反转数组
# print listA, listB
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
