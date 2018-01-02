# 定义集合
s1 = {2, 4, 6, 8, 10, 12, 14, "1", "2"}
s2 = frozenset({1, 2, 3, 4, "1", "2"})

s3 = frozenset({1, 2, 3, "1", "2"})
# s3 = s2.intersection(s1, s2, s3)
# s3 = frozenset.intersection(s2, s1, s3)

# s3 = s2 & s1 & s1
# print(s1, s2, s3, sep="  ,  ")

# s3 = set.intersection_update(s2, s3)

# 并集
# s3 = s3 | s2 | s3
# s3 = s1.update(s2, [1, 2,  5, 7])
# 差级
s3 = s1.difference(s3)

print(s1, s2, s3, sep="  ,  ")


