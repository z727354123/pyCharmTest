# 定义 一个可变集合
# s = {1, 2, 3, 5, 3}
# print(s)
# print(type(s))
#
# for i in s:
#     print(i)

# 使用 set( iterable )
# dic = [ [2, 1], [1, 2] ]
# print(dic)
#
# s = set(dic)
# # print(s)

# 集合推导式
# s = {item for item in "abc"}
# print(s)
# s = set(item for item in "asd")
# print(s)


# 不可变集合
s = frozenset(item for item in "dsfgasdfh")
print(s)

for i in s:
    print(i)


# 定义 空集合
s = set()
print(s)
print(type(s));
s = frozenset()
print(s)
print(type(s));

#  list 去重
listA = [1, 2, 4 ,5, 2, 3,5]
s = frozenset(listA)
listA = list(s)
print(listA)