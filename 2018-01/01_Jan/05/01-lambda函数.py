# lambda函数
# lambda 参数1 , 参数2 : 返回值表达式
res = lambda x, y : x * y
print(res(3, 4))

res = (lambda x, y: x + y)(40, 50)
print(res)


# 闭包

def res (a) :
    def newx() :
        print(a)
    return newx

res = res(110)
res()
res()
res()

