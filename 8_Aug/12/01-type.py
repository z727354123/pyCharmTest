import math as myMath
num = 12e999
print(num)
print(type(num))

print(type('stringA'))
print(type(123e1))
print(type(123e8))
print(type(False))
print(type(type))
print(type(str))
print(type(print))
print(type(type(123)))

print('\n----------------\n')
# inf 与 ninf 和 nan
inf = float('inf')
ninf = float('-inf')
nan = float('nan')
print(inf)
print(ninf)
print(nan)
print(inf is inf)
print(inf == inf)
print(inf is float('inf'))
print(inf == float('inf'))
print(ninf == -inf)
print('----------------')
print(nan is nan)
print(nan == nan)
print(nan is float('nan'))
print(nan == float('nan'))

print('\n-------判断 是否是 inf 或 nan---------\n')
# 判断 是否是 inf 或 nan
print(myMath.isinf(inf))
print(myMath.isinf(ninf))
print(myMath.isinf(nan))
print(myMath.isnan(inf))
print(myMath.isnan(nan))
print(myMath.isnan(myMath.nan))


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
