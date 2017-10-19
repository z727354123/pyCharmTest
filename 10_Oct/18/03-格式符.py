numOne = 998
numTwo = 123

# name
# 手机卖998，鼠标卖123
print("手机卖%d，鼠标卖%d" % (numOne, numTwo))

# 手机卖998，鼠标卖123
print("手机卖%(1)d，手机卖%(1)d，鼠标卖%(2)d" % ({
    '1': numOne,
    '2': numTwo
}))

# 报错
# print("手机卖%(1)d，鼠标卖%d" % ({
#     '1': numOne
# }, numTwo))

# width 占位数
print('%2d' % numTwo)   # 123
print('%4d' % numTwo)   #  123

# flag -左对齐
print('%-5d' % numTwo, end='END\n')     # 123  END
# flag ' ' or 多个 ' '  正数前面 加一个空格
print('% d' % numTwo, end='END\n')      #  123END
print('%     d' % numTwo, end='END\n')  #  123END
print('%     d' % -numTwo, end='END\n') # -123END
# flag 0 表示用 0填充
print('%05d' % numTwo, end='END\n')     # 00123END
print('%(min)02d:%(sec)02d' % ({        # 07:06
    'min': 7,
    'sec': 6
}))


