myStr = 'string'
print(myStr[-6])
print(myStr[5])
# 下面都越界了
# print(myStr[-7])
# print(myStr[6])

# list 操作
myList = ['just', 'for', 'you']
myStr = ','.join(myList)
print(myStr)
myList = myStr.split(',')
print(myList)

# 步长值
print(myStr[::2])
print(myList[::2])
print(myStr[::-1])
print(myList[::-1])
print(myList[0:len(myList):-1])
print(myList[len(myList):-len(myList)-1:-1])