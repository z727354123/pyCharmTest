# 函数
def myFun(num1, num2):
    print(num1)
    print(num2)

# 引入 functools
import functools
newFun = functools.partial(myFun, num1 = 31, num2 = 56)

newFun()
