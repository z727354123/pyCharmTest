# 拆包
def otherFun (num1, num2, num3 = {"name":123}):
    print(num1 + num2 + num3)

def myFun (num1, *args):
    otherFun(*args)

myFun(1, 2, 3, 4)   # 2+3+4 = 9

print(*[3, 5, 6])
dicA = {"name": "lisi", "age": 12}
print({"name": 1234, **dicA})
print({**dicA, "name": 1234})
# JS6 ... 这种dict 拆包
# 谁在后面 谁覆盖谁

def myFun (str1, str2):
    print(str1, type(str1))
    print(str2, type(str2))

# myFun(*dicA)
print(type(myFun))
print(myFun)
