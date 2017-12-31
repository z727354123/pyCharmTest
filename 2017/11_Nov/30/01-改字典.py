# 1. 修改单个字典
dictA = {}

dictA['name'] = '李四'
dictA[123] = '王五'

print(dictA)
# {'name': '李四', 123: '李四'}

# 2. 修改多个 键值对
dictA.update({'nameTwo': '张三', 123: '不是王五'})

print(dictA)
# {'name': '李四', 123: '不是王五', 'nameTwo': '张三'}






