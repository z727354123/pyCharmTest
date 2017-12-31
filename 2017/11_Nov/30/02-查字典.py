# 方式一，dic[key]
# 不存在，报错
dic = {'name': '李四', 'age': 18}

print(dic['name'])
# 李四
# print(dic['not'])
# KeyError: 'not'


# 方式二，dic.get(key[, default])
# 如果不存在，没有default，返回 None
# 如果不存在，有default，返回 default
dic = {'name': '李四', 'age': 18}
print(dic.get('name'))
# 李四
print(dic.get('not'))
# None
print(dic.get('not', 'Nothing'))
# Nothing
print(dic)     # 说明 key 仍然不存在
# {'name': '李四', 'age': 18}

print('------------------华丽的分割线------------------')

# 方式三，dic.setdefault(key[, default])
# 如果key存在，返回具体值，default 没有任何作用。
# 如果key不存在，没有default，返回 None，且设置 dic[key] = None
# 如果key不存在，有default，返回 default，且设置 dic[key] = default
dic = {'name': '李四', 'age': 18}
print(dic.setdefault('name'))
print(dic)
# 李四
# {'name': '李四', 'age': 18}
print(dic.setdefault('name', 'XX'))
print(dic)  # 说明 已存在的 value 不会窜改
# 李四
# {'name': '李四', 'age': 18}
print(dic.setdefault('not'))
print(dic)
# None
# {'name': '李四', 'age': 18, 'not': None}
print(dic.setdefault('not2', 'Nothing'))
print(dic)
# Nothing
# {'name': '李四', 'age': 18, 'not': None, 'not2': 'Nothing'}





