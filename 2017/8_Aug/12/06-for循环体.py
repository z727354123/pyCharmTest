string = "String"
num = 1
for i in string:
    print(i, end=" " + str(num) + "\n")
    num += 1

myList = ['李四', '张三XX']
for i in myList:
    print(i, len(myList), len(i))
print(list(myList))
print(myList)

print('\n--------------\n')

for i in range(1):
    print(i)
else:
    print('enter Else')

print('\n--------------\n')

for i in range(1):
    print(i)
    if i == 0:
        break
else:
    print('enter Else')
