boolA = True
boolB = True
boolC = False
print(True or True and False)     # True
print((True or True) and False)   # False
print(True or (True and False))   # True  说明 and 优先级 > or


print(not True and False)     # False
print(not False and True)     # True 说明 not 优先级 > and

