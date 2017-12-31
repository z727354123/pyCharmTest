# _*_ coding:utf-8 _*_
# 定义一个字典
d = {"name": "李思思", "age": 31}


# 获取 所有的 value
listA = d.viewvalues()
print listA

d[10086] = 1111;
print listA

for item in listA:
    print item
#
#
#
#
#
#
#
#
#
# # 获取 所有的 键值对
# listA = d.items();
# print(listA)
#
#
#
#
#
# # 获取 所有的 key
# listA = d.keys();
# print(listA)