myStr = ''
print(myStr.isalnum())      # False 不支持空
myStr = 'abCC'
print(myStr.isalpha())      # True 支持大写
myStr = 'abc*'
print(myStr.isalpha())      # False 不支持 符号
myStr = 'abc1'
print(myStr.isalpha())      # False 不支持 包含num
print(myStr.isalnum())      # True 支持  包含num
myStr = '123'
print(myStr.isnumeric())    # True 只支持 全数字
myStr = '123.123'
print(myStr.isnumeric())    # False
myStr = '0.1'
print(myStr.isnumeric())    # False 不支持 .
print(myStr.isalnum())    # False 不支持 .
myStr = 'abc123.1'
print(myStr.isalnum())    # False 不支持 .

