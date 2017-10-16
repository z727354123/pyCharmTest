strA = '123'
strB = '123'
strA = strA + '4'
strB = strB + '4'
print(strA, strB)
print(strA is strB)    # False
print(strA is '1234')  # False
print(strB is '1234')  # False
print(strA == strB)
