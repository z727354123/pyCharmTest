# 迭代器
# listA = [1, 2, 3, 4]
# i = iter(listA)
#
# print(next(i))
#
# listA[0] = 998
# del listA[1]
#
# listA.insert(0, "XXXOO")
#
# print(next(i))
# print(next(i))
# print(next(i))

# dict
listA = {"name":"李四", "age": 18, 'son':'no'}
it = iter(listA)

# del listA["age"]

print(type(next(it)))

import collections;
print(isinstance(it, collections.Iterable ))
print(isinstance(listA, collections.Iterable ))
# 报错: RuntimeError:
# dictionary changed size during iteration


# for i in it:
#     print(i)


