# range 0 ~ 5
print(range(5, 2))
print(type(range))

print(list(range(5, 2)))
print(list(range(0, 6, 2)))

for i in range(5):
    print(i, end=', ')

print('\n\n------range 与 list 区别--------')
# range 与 list 区别
ran = range(1, 6)   # 含头不含尾 1, 2, 3, 4, 5
lis = [1, 2, 3, 4, 5]
print(ran)
print(lis)
print(type(ran))
print(type(lis))
print(list(ran) == lis)

a = range(lis)
print(a)
