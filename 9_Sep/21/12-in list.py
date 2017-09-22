
print(123 in [1, 123])
print(123 not in [1, 123])
print(234 in [1, 233])
print(234 not in [1, 233])


listA = [1]
listC = [1]
listB = [1, 2, 3, 4, listA]

print('------------')
print(listA in listB)
print(listC is listA)
print(listC == listA)
print(listC in listB)

print('------------')
print('asd' in 'faddddasdf')
print('123' is '123')
print(123 is 123)
