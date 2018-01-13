# 遍历对象本身
# f = open("a.txt", encoding="utf-8")
# for i in f:
#     print(i, end="")

# 容错处理
# f = open("a.txt", encoding="utf-8")
# # 判断对象 是否 可读
# print(f.readable())
# # 判断对象 是否 可写
# print(f.writable())

# write 返回
f = open("a.txt", "a+",encoding="utf-8")

# 容错处理
if f.writable():
    # 打印 添加字节数
    print(f.write("我是添加内容"))

f.close()