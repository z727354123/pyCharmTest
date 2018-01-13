# 文件操作 读
# 1. 打开文件
# r 模式 特性，导致找不到 会报错
# FileNotFoundError: [Errno 2] No such file or directory: 'a.txt'
# a = open("a.txt", "r+", encoding="UTF-8")       # 两句话等效
# b = open("a.txt", "r+", encoding="UTF-8")  # mode 默认是 "r"
# print(a)
# print(b)
#
#
# # 2. 读取文件
# contentA = a.read()
# print(contentA) # 我是原本的内容
# # b.write("My")
# # UnicodeDecodeError: 'utf-8' codec can't decode
# # byte 0x91 in position 0: invalid start byte
# b.write("呵呵")
#
# contentB = b.read()
# print(contentB) # 原本的内容
# b.write("End")
# b.close()
#
# contentA = a.read()
# print(contentA) # End 注意 b.close 才会有
# a.write("A")
#
# a.close()


# 文件操作 写
import time
# 1. 打开文件
a = open("a.txt", "a+")  # 这句代码 会清除 原本的 a.txt
b = open("a.txt", "a+")
print(a)
print(b)

time.sleep(2)
# 2. 读取文件
# w 模式 无法 read()
# io.UnsupportedOperation: not readable
b.write("BBB\n")
print("b wriete")
b.read()  # 立刻写入，
time.sleep(2)

contentA = a.read()
print("contentA", contentA)
time.sleep(2)


a.write("AAAA\n")
a.close()   # 立刻写入，

time.sleep(2)

contentB = b.read()  # read() 操作 也会把之前的写入
print("contentB", contentB)
b.write("BBB\n")
time.sleep(2)
b.close()   # 立刻写入，替换改变的 内容

# b2 = open("a.txt", "w+")
# b2.close()
# print("b2 end clean")
# time.sleep(2)


# 文件操作 末尾写
# import time
# # 1. 打开文件
# time.sleep(2)
# a = open("a.txt", "a", encoding="utf-8")  # 若 a.txt 不纯在则创建
# b = open("a.txt", "a")
# print(a)
# print(b)

# 2. 读取文件
# w 模式 无法 read()
# io.UnsupportedOperation: not readable
# contentA = a.read()
# contentB = b.read()

# 3. 写入文件
# b.write("BBBB\n")     # 不会立刻写入
# b.write("2222\n")
# time.sleep(2)
# print("b write end, a close")
# a.write("钟文杰\n")
# a.write("1111\n")
#
# # 4. 关闭文件
# a.close()   # 立刻写入，在 a.txt  末尾追加，
#             # 若 a.txt 不见了，不做任何操作
#             # w 模式 也是 这样 不做任何操作
#
# time.sleep(2)
# b.close()   # 立刻写入，在 a.txt  末尾追加，
# print("b  close")
