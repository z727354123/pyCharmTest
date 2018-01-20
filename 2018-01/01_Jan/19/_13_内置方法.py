# 内置方法
def printDict(dictA):
    for item, val in dictA.items():
        print(item + " : ", val)

# printDict(object.__dict__)

obj = object()

# obj.__dict__['name'] = "123"
# print(obj.__dict__)
print(obj.__dir__())