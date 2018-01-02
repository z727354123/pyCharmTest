# 可变集合
s = {1, 2, 6}
b = frozenset({4, 5, 6})
# 增
# set.add(s, 3)
# s.add(6)
# print(s, type(s))
# print(b, type(b))
# 删
# a = s.remove(1)
# a = s.discard(4)
# a = s.pop()
# a = s.pop()
# a = s.pop()
# a = s.pop()
# a = s.clear()
# a = s.clear()
# a = s.clear()

# 改
# 元素为不可变类型，无法修改

# 查
# for in 查询
# for i in b:
#     print(i)
# 迭代器
i = iter(b)
print(next(i))
print(next(i))
print(next(i))
