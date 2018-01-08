# 作用域测试
b = 10

def test():
    print(__name__)
    print(b)


b+=10
test()

print(b)

print(__name__)


