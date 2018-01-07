# 装饰器
def myFun(char):
    print("muFun char: " + char)
    def decorator(func):
        print("decorator char: " + char)
        def inner(*args, **kwargs):
            print(char * 10)
            return func(*args, **kwargs)
        return inner
    return decorator


# 函数
@myFun("+")
@myFun("-")
def test (num1 = 99):
    print(num1)
    return "xx"


test();






