listOne = ['李四', '张三']
print(listOne)

one = listOne.append('小明')
print(one)
print(listOne)

listTemp = ['李四2', '李四3']
one = listOne.extend([])
print(one)
print(listTemp)

listTwo = list.extend(listOne, ['cc'])

print(listTwo)
print(listOne)

