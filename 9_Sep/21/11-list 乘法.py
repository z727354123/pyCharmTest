listA = [1]
listB = [1, 2, 3, 4, listA]

listA *= 1
print(listB * 1)
listB *= 1
print(listB)
listB *= 1
print(listB)

