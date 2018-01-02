# 定义集合
s1 = {1, 2, 3}
s2 = {1, 2}

# 是否有交集
# print(s1.isdisjoint(s2))

# 是否包含
# print(s1.issuperset(s2))
# print(set.issuperset(s2, s1))

print(s1.issubset(s2))
print(s2.issubset(s1))