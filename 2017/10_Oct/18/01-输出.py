# _*_coding:utf-8 _*_
name = '李四'
age = 18
# 注意 %s 只能 小写 s
# 注意 %d 代表 10进制 数值
print("我的名字是：%s，我的年龄是：%d!" % (name, age))

print("我的名字是：{0}，{0}的年龄是：{1}!".format(name, age))
# 我的名字是：李四，我的年龄是：18!

# 输出到文件 中
f = open('test.txt', 'w')
print("XXXXX", file=f)


