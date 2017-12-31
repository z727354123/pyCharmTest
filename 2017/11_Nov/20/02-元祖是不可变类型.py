dictA = {'name': '李四'}
# TypeError: unhashable type: 'dict'
# tupleA = (1, dictA)
# 元组做 key 时，里面不能 有 可变类型
tupleA = (1, 2, 3, 5)
dictB = {tupleA: 123}
print(dictB)
# {(1, 2, 3, 5): 123}
print({(5, 3, 2, 1): 10086})
# {(5, 3, 2, 1): 10086}
print({(5, 3, 2, (2, 4)): 10086})
# {(5, 3, 2, (2, 4)): 10086}

