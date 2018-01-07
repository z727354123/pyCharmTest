# 定义一个装饰器
def decorator(func):
    def inner(*args, **kwargs):
        print(args, kwargs)
        print("-" * 30)
        return func(*args, **kwargs)
    return inner



# 有参数的 函数
@decorator
def demo(num1, num2, num3):
    print(num1, num2, num3)
    return num2


# demo(342, num2="111", 654165)
# 报错 SyntaxError:
# positional argument follows keyword argument
# 最后一个 之前有 key=value, 最后一个必须 key=value
res = demo(342, num2="111",  num3=654165)
print(res)


