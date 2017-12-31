# _*_ encoding:utf-8 _*_
# cmp() 比较函数
# print cmp(10, 1)      # 1
# print cmp(10, 10)     # 0
# print cmp(10, 11)     # -1
# print cmp('a', 'b')   # -1
# print cmp('a', 'A')   # 1
# print cmp('a', 'a')   # 0
# print cmp('a', 'aa')   # -1
# print cmp('我', '你')   # 1
# print cmp('我', '是')   # -1
# print cmp('啊', '吧')   # 1
# print cmp('吧', '爱')   # -1
# print cmp('在', '月')   # -1 按拼音 顺序

def cmp(one, two):
    if one == two:
        return 0
    elif one > two:
        return 1
    return -1


print(cmp(10, 1) == 1)  #
print(cmp(10, 10) == 0)  #
print(cmp(10, 11) == -1)  #
print(cmp('a', 'b') == -1)  #
print(cmp('a', 'A') == 1)  #
print(cmp('a', 'a') == 0)  #
print(cmp('a', 'aa') == -1)  #
print(cmp('我', '你') == 1)  #
print(cmp('我', '是') == -1)  #
print(cmp('啊', '吧') == 1)  #
print(cmp('吧', '爱') == -1)  #
print(cmp('在', '月') == -1)  # 按拼音 顺序
