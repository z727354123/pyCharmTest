
print(type('stringA'))
print(type(type(123)))
print(type(123e1))
print(type(123e8))
print(type(False))
print(type(print))
print(type(type))

print('\n----------------\n')

print(isinstance('a', str))
print(isinstance(type, str))
print(isinstance(type, type))
print(isinstance(str, type))
print(isinstance(int, type))
print(isinstance(int, type))

print('\n----------------\n')

print(isinstance(int, int))
print(isinstance(str, str))
print(isinstance(print, type))
print(isinstance(float, type))
print(isinstance(int, type)) 
print(isinstance(str, type))
