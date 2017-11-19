# 字典 转 元组 & 列表
# 只会 转 key
dictA = {'0': '李四', '1': 18}
print(dictA)
print(list(dictA))
print(tuple(dictA))
# {'0': '李四', '1': 18}
# ['0', '1']
# ('0', '1')

# 字典转 key 定义
name = 123
age = 'age'
dictA = {name: '李四', age: 18, True: 10086, False: 'hehe®', 1: 'xxx'}
print(dictA)
# {123: '李四', 'age': 18, True: 'xxx', False: 'hehe®'}
dictA = {name: '李四', age: 18, 1: 'xxx', True: 10086, False: 'hehe®'}
print(dictA)
# {123: '李四', 'age': 18, 1: 10086, False: 'hehe®'}
# 基本数据 类型 都可以 做 key
# True = 1
# False = 0
# True & 1 哪个先出现，哪个就是 key
print(dictA[1])
print(dictA[True])
# 都是 10086
print('------------------华丽的分割线------------------')

# 字典转 迭代器
dictA = {
    'name': '李四',
    'age': 18
}


iterA = iter(dictA)
res = next(iterA)
print(res)
res = next(iterA)
print(res)

