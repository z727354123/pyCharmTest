tupleA = '123', 'xxx', [456.0, 1230.0, 444]

x, y, z = o = 123, 23, [123]

print(type(x))
print(y)
print(z)

print('\n-------------\n')
x, y, z = tupleA
print(type(x))
print(y)
print(z)

print('\n-------------\n')
x, y, z = tupleA[2]
print(type(x))
print(y)
print(z)

print('\n-------------')
print(o)


