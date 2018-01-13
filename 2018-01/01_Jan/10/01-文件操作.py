# __name__ 测试
# def test():
#     print(123, __name__)
#     def inner():
#         print("inner")
#         print(__name__)
#     inner()
#
# test()


# 文件操作 读
# 1. 打开文件


# r 模式 特性，导致找不到 会报错
# FileNotFoundError: [Errno 2] No such file or directory: 'a.txt'
# a = open("a.txt")       # 两句话等效
# b = open("a.txt", "r")  # mode 默认是 "r"
# print(a)
# print(b)
#
# # 2. 读取文件
# contentA = a.read()
# contentB = b.read()
#
# print(contentA)
# print(contentB)
#
# # 3. 写入文件
# # io.UnsupportedOperation: not writable
# # a.write("XXOO")
# # b.write("BBoo")
#
# # 4. 关闭文件
# a.close()
# b.close()

# # 文件操作 写
# import time
# # 1. 打开文件
# time.sleep(2)
# a = open("a.txt", "w")  # 这句代码 会清除 原本的 a.txt
# b = open("a.txt", "w")
# print(a)
# print(b)
#
# # 2. 读取文件
# # w 模式 无法 read()
# # io.UnsupportedOperation: not readable
# # contentA = a.read()
# # contentB = b.read()
# # print(contentA)
# # print(contentB)
#
# # 3. 写入文件
# b.write("4")     # 不会立刻写入
# b.write("B")
# time.sleep(2)
# a.write("XXOO")
# a.write("XXOO22AAA")
#
# # 4. 关闭文件
# a.close()   # 立刻写入，替换原来的 a.txt
# time.sleep(2)
#
# b.close()   # 立刻写入，替换原来的 a.txt

# 文件操作 末尾写
import time
# 1. 打开文件
time.sleep(2)
a = open("a.txt", "a", encoding="utf-8")  # 若 a.txt 不纯在则创建
b = open("a.txt", "a")
print(a)
print(b)

# 2. 读取文件
# w 模式 无法 read()
# io.UnsupportedOperation: not readable
contentA = a.read()
contentB = b.read()
print(contentA)
print(contentB)
# 3. 写入文件
b.write("BBBB\n")     # 不会立刻写入
b.write("2222\n")
time.sleep(2)
print("b write end, a close")
a.write("123\n")
a.write("1111\n")

# 4. 关闭文件
a.close()   # 立刻写入，在 a.txt  末尾追加，
            # 若 a.txt 不见了，不做任何操作
            # w 模式 也是 这样 不做任何操作

time.sleep(2)
b.close()   # 立刻写入，在 a.txt  末尾追加，
print("b  close")
