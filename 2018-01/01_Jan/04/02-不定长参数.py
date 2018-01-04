# 定义一个不定长参数 函数
def muFun (*args) :
    print(args, type(args))
    print(args, len(args))
    # print(args[0], type(args[0]))

# muFun(2, 3, 4)
# muFun([2, 3, 4])
# muFun()


# 字典函数 组合1
def muFun (num1, *args,**kwargs) :
    print(num1, args, kwargs)

# muFun(444, 123,34 ,name = 123)
# muFun(444, 123,34 ,num1 = 1)
# got multiple values for argument 'num1'


# 字典函数 组合2
def muFun (num1, *args, num2 , **kwargs) :
    print(num1, num2, args, kwargs)

muFun(444, 34, num2=123, name = "XXX" )
# muFun(444, name = "XXX" , 34, num2=123 )
# positional argument follows keyword argument
muFun(444, num2=123)

# def myFun (*args) :
#     print(num1)
#
# myFun(1,name =1 )






