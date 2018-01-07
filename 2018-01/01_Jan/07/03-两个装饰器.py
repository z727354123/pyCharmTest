# 定义装饰器
def decorator1 (func):
    print(1)
    def inner ():
        print("decorator 1")
        func();
    return inner

def decorator2 (func):
    print(2)
    def inner ():
        print("decorator 2")
        func();
    return inner

@decorator1
@decorator2
def test():
    print("test")

# test = decorator2(test)
# test = decorator1(test)

test()

