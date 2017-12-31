o = [666, 123, 234]

# x, y = o # ValueError: too many values to unpack
# x, y = 999 # TypeError: 'int' object is not iterable
# print(x)
# print(y)

a = {x for x in 'abracadabra' if x not in 'abc'}
b = [x for x in 'abracadabra' if x not in 'abc']
c = (x for x in 'abracadabra' if x not in 'abc')
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
