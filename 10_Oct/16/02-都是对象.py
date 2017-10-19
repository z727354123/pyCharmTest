strA = '123'
print(id(strA))
strB = '123'
print(id(strB))
strA = strA + '4'
print(id(strA))
strB = strB + '4'
print(id(strB))
print(strA, strB)
print(strA is strB)    # False
print(strA is '1234')  # False
print(strB is '1234')  # False
print(strA == strB)    # True
num = 10
print(1 < num > 5)     # True
