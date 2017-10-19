flag = True
while flag:
    strA = input("输入0停止")
    if strA == '0':
        flag = False
        continue
    strA = input("输入1停止")
    if strA == '1':
        flag = False
        continue
    strA = input("输入2。没有else")
    if strA == '2':
        break
else:
    print('else')
print('over')
