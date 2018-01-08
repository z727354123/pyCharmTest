# send方法
def test():
    for i in range(1, 100):
        print("befor = " + str(i))
        res = yield i
        print("res = " + str(res))

iterA = test()

# print(iterA.send(1))  报错
# TypeError: can't send non-None value
# to a just-started generator

print(iterA.send(None))
print("-"*30)
print(iterA.send(5))
print("-"*30)
print(iterA.__next__())
