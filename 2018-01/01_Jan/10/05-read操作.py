# #
# f = open('a.txt', 'r', encoding="UTF-8")
#
# print(f.read(3))
# print(f.read(3))
# print(f.read(3))
#
# f.close()


# f = open('a.txt', 'r', encoding="UTF-8")
#
# print(f.readline(12), end="")   # 读到 第12个字节
# print(f.readline(), end="") # 读了一个回车
# print(f.readline(9999), end="") # 读到回车就结束
# print(f.readline(), end="") # 读了 33
# # print(f.readline(), end="")
#
# f.close()
import time

f = open('a.txt', 'r+', encoding="UTF-8")

f.write("里");

time.sleep(2)
print("seek")
f.seek(3)

time.sleep(2)
f.write("何")

print("close")
f.close()










