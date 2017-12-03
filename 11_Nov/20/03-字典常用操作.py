# 增加操作
dictA = {'name': '李四', 'age': 18}
dictA['level'] = '超凡大师'
print(dictA)
# {'name': '李四123', '1age': 18, 'level': '超凡大师'}


# 删除操作
# del 是语句，没有返回值
dictA = {'name': '李四123', '1age': 18, 'level': '超凡大师'}
del dictA['name']
print(dictA)
# {'1age': 18, 'level': '超凡大师'}
# del dictA['name']
# KeyError: 'name'
# 不能 del 不存在的 属性, 报错


# pop(key[, default]) 方法
dictA = {'na me': '李四123', 'age': 18, 'level': '超凡大师'}
res = dictA.pop('level')
print(res)
# 超凡大师
print(dictA)
# {'name': '李四123', 'age': 18}

# res = dictA.pop('level') 同样不可以 pop
# KeyError: 'level'
res = dictA.pop('level', '青铜五')
print(res)
# 青铜五

print('------------------华丽的分割线------------------')

# popitem() 方法
# 返回最后 初始化的 key， 返回 元组
dictA = {'level': '李四123', 'age': 18, 'name': '超凡大师'}
res = dictA.popitem()
print(res)
# ('level', '超凡大师')
print(dictA)
# {'name': '李四123', 'age': 18}

dictA = {'123': '李四123', 'age': 18, 'level': '超凡大师'}
dictA['231'] = {'hehe': 'I\'m Dict'}
res = dictA.popitem()
print(res)
# ('name1', {'hehe': "I'm Dict"})
print(dictA)
# {'name': '李四123', 'age': 18, 'level': '超凡大师'}


dictA = {}
dictA.popitem()
# KeyError: 'popitem(): dictionary is empty'
