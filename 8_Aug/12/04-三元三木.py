while True:
    num = input('请输入一个数字A，让我猜猜范围:')
    trueMsg, falseMsg = 'A大于等于10', 'A小于10'
    print((trueMsg if int(num) >= 10 else falseMsg) + '对吗？')
    num = int(input('输入0终止程序'))
    if num == 0:
        break

# 再来一次 三元运算符号
print(trueMsg)
