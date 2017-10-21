# 2进制
print(0b10)     # 2
# 8进制
# print(010)     # 语法错误
print(0o10)     # 8
# 16进制
print(0x1e)     # 30

# 转 2进制
print(bin(0b10))    # 0b10
print(bin(0o10))    # 0b1000
print(bin(10))      # 0b1010
print(bin(0x10))    # 0b10000
# 转 8进制
print(oct(0b10))    # 0o2
print(oct(0o10))    # 0o10
print(oct(10))      # 0o12
print(oct(0x10))    # 0o20
# 转 10进制
print(int(0b10))    # 2
print(int(0o10))    # 8
print(int(10))      # 10
print(int(0x10))    # 16
# 转 16进制
print(hex(0b10))    # 0x2
print(hex(0o10))    # 0x8
print(hex(10))      # 0xa
print(hex(0x10))    # 0x10


print(not 0)                # True
print(not complex(0, 0))    # True
print(not complex(9, 0))    # False
print(not complex(0, 9))    # False
