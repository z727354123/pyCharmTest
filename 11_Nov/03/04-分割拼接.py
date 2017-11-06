# split 方法
myStr = '123,345,21345'
# print(myStr.split())    # 空参数，直接一个 list 包裹
# print(myStr.split(',', 1))    # 从左开始分割
# print(myStr.split(',', -1))    # 默认值 -1

# partition 方法
myStr = '123,345,21345'
# print(myStr.partition('213'))   # 返回三个元素的 tuple
# print(myStr.partition('1111'))   # 没找到就 tuple[1] = tuple[2] = ''
# print(myStr.partition('21345'))   # 找到末尾， tuple[2] = ''
# print(myStr.partition('123'))   # 找到开头， tuple[0] = ''
# print(myStr.partition('345'))   # 从左往右找

# splitlines 方法
# myStr = '\r wo  \n  shi  \r  lisi \r'
# print(myStr)
# print(myStr.splitlines())   # 最后一个\r 不算 \r\r 算一个
# print(myStr.splitlines(True))   # 默认 False

# join 方法
myStr = ',,'
# 不能 join 数字 list
# print(myStr.join([1, 2, 3, 4])) TypeError: sequence item 0: expected str instance, int found
print(myStr.join(['1', '2', '3', '4'])) # 可以拼接 String