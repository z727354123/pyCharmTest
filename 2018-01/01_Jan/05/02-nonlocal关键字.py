# 不能 在定义前使用
# num = 100;
# def myFun():
#     print(num)
#     num = 555
#
# myFun()

# 不支持 全局变量
# num = 100
# def myFun():
#     nonlocal num
#     print(num)
#
# myFun()

# 定义方法
# def myFun(num1, num2, num3):
#
#     def myTest():
#         num2 = 22   # 不能再声明之前初始化
#         nonlocal num2, num3
#         num1 = 11
#         num3 = 33
#         print(num1, num2, num3)
#
#     print(num1,num2, num3)
#     myTest()
#     print(num1,num2, num3)
#
# myFun(1 , 2, 3)


# 定义方法
def myFun(num1, num2, num3):

    def myTest():
        num4 = 22   # 无关 因素
        nonlocal num2, num3
        num1 = 11
        num3 = 33
        print(num1, num2, num3)

    print(num1,num2, num3)
    myTest()

    print(num1,num2, num3)
    num2 = 123
    num3 = 333
    return myTest

fun = myFun(1 , 2, 3)

fun()