# list.sort() 方法
myList = [
    (4, 1),
    (1, 4),
    (2, 3),
    (3, 5),
    (5, 2)
]
print(myList.sort())    # None
print(myList)
# [(1, 4), (2, 3), (3, 5), (4, 1), (5, 2)]

def getKey(item):
    return item[1]

print(myList.sort(key=getKey))    # None
print(myList)
# [(4, 1), (5, 2), (2, 3), (1, 4), (3, 5)]

print(myList.sort(reverse=True))    # None
print(myList)
# [(5, 2), (4, 1), (3, 5), (2, 3), (1, 4)]

