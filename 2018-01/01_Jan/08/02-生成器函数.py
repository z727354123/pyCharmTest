# 函数方式 表示
def test():
    for i in range(1, 5000):
        yield i
        print("yield  = " + str(i))
        return

res1 = test()
res2 = test()

print(res1, type(res1))
print("next(res1) = " + str(next(res1)))
print("next(res1) = " + str(next(res1)))

print(res2, type(res2))
print("next(res2) = " + str(next(res2)))
print("next(res2) = " + str(next(res2)))
