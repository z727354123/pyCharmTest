listA = [1, 2, 3, 4]
listB = [1, 2, 3, 4, listA]

listB.remove(4)
print(listB)

listA.remove(4)
print(listB)

del listB[-1]
print(listB)
