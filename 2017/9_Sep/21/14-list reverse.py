listA = [1]
listB = [1, 2, 3, 4, listA]
listC = [1]

listB *= 3
listA *= 3

print(listB)
print(listB.reverse())
print(listB)

