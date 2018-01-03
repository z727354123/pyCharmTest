# datetime 模块
import datetime

# print(datetime.datetime)
# print(datetime.datetime.now())
# print(type(datetime.datetime.now()))
# print(datetime.datetime.today())
# print(type(datetime.datetime.today()))


# t = datetime.datetime.now()
#
# print(t.year)
# print(t.month)
# print(t.day)
# print(t.hour)
# print(t.minute)
# print(type(t.year))
# print(type(t.month))
# print(type(t.hour))
# print(type(t.day))
# print(type(t.second))
# print(type(t.minute))


# 计算 3.5 天后 的日期
# t = datetime.datetime.now()
#
# res = t + datetime.timedelta(days=3.5)
#
# print(type(datetime.timedelta(days=3.5)))
# print(t)
# print(res)

# 获取两个 日期的 时间差
s1 = datetime.datetime(2017, 1, 1)
print(s1)
s1 = datetime.datetime(2017, 1, 1, 10)
print(s1)
s1 = datetime.datetime(2017, 1, 1, 10, 55)
print(s1)
s1 = datetime.datetime(2017, 1, 1, 10, 55, 44)
print(s1)
s1 = datetime.datetime(2017, 1, 1, 10, 55, 44, 12345)
print(s1)

first = datetime.datetime(2017, 1, 2)
end = datetime.datetime(2017, 1, 2, 10)
temp = end - first
print(temp)
print(type(temp))

print(temp.total_seconds())







