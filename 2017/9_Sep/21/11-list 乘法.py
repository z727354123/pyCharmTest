listA = [1]
listB = [1, 2, 3, 4, listA]

print(listB)
listB *= 2
print(listB)
listA *= 2
listB *= 2
print(listB)

