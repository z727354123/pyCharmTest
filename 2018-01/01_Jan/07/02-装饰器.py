# 装饰器

# 定义装饰方法
def checkLogin(func):
    def inner():
        # 需要添加的操作
        print("我是额外操作")
        print("但是只能在目标方法前面调用")
        func()
    # return "xxxx"
    return inner

# 需要装饰的 函数
# 只能装饰在前面
@checkLogin
def fss():
    print("发说说")


# fss = checkLogin(fss)
# print(fss)
fss()