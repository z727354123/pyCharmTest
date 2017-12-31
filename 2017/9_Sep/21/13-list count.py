listA = [1]
listB = [1, 2, 3, 4, listA]
listC = [1]

listB *= 3
print(listB)
print(listB[9] == listA)
print(listB[4] is listA)
print(listB[9] is listA)
print(listB[9] is listC)
print('-------------------------')
print(listB.count(listA))
print(listB.count(listC))
print(listB.index(listC, 5))
print(listB.index(listC, 5, 10))
print('-------------------------')
listA *= 3
print(listB)

