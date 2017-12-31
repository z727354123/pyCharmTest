myStr = ' 我str '
print(myStr.islower())  # True  全字母 小写 + 其他 非大写字母 即可
myStr = ' 我STR '
print(myStr.isupper())  # True
myStr = ' 我Str '
print(myStr.islower())  # False
print(myStr.isupper())  # False
print(myStr.isspace())  # False
myStr = ' a '
print(myStr.isspace())  # False
myStr = ' '
print(myStr.isspace())  # True 必须 纯空格
