myStr = 'String'
print(myStr.ljust(10, '0'))

# lstrip
myStr = '  \n 123   '
print('|' + myStr.lstrip() + '|')
print('|' + myStr + '|')

myStr = 'wwwwxxxxxoooooxxxxxwww 123 '
print('|' + myStr.lstrip('123oxw') + '|')
print('|' + myStr.rstrip('123 w') + '|')
print('|' + myStr + '|')
