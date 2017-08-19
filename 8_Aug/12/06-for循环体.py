string = "String"
num = 1
for i in string:
    print(i, end=" " + str(num) + "\n")
    num += 1

myList = ['李四', '张三1']
for i in myList:
    print(i, len(myList), len(i))
print(list(myList))
print(myList)

