# 引入 time 模块
import time
import calendar
# 获取 时间戳
# num = time.time()
# print(num, type(num))
# print(num / 60/ 60 /24 / 365)

# 获取 时间元组
tuperA = time.localtime(time.time() + 3600 * 24 * 5)
# print(tuperA, type(tuperA))

# 格式化时间
# s1 = time.ctime()
# s1 = time.asctime(tuperA)

# 自定义 格式时间
# s1 = time.strftime("%y-%m-%d %H:%M:%S")
# print(s1)
# print(tuperA)
# print(type(s1))

# 字符 转 时间
# s1 = time.strptime("18", "%y")
# print(s1)
# print(type(s1))
# s1 = time.mktime(s1)
# print(s1)
# print(type(s1))

# 获取 CPU 当前时间
# s1 = time.clock()
# print(s1)
# print(type(s1))
#
# time.sleep(2)
# for i in range(0, 10000000):
#     a = i * i
#
# s1 = time.clock()
# print()
# print(s1)
# print(type(s1))

# 获取 日历文本
s1 = calendar.month(1, 1)
print("-----------")

print(s1)

print("-----------")


