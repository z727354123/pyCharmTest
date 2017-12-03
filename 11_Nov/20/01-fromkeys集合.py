# dict.fromkeys 静态方法
dictA = dict.fromkeys('abc')
print(dictA)
# {'a': None, 'b': None, 'c': None}
# 把 seq 分解成 key

dictA = dict.fromkeys('abc', 666)
print(dictA)
# {'a': 666, 'b': 666, 'c': 666}
# 每个 key 的 val 都是 666

# fromkeys 静态方法 对象调用
dictA = {'name': '李四'}
print(dictA)
print(dictA.fromkeys('qwe', 777))
# {'name': '李四'}
# {'q': 777, 'w': 777, 'e': 777}
# 对象调用该方法，，意义不大
# 所以 一般都用 类调用静态方法

# string 跟 number key 不一样
dictA = {1: 123, '1': 321, '': 435, False: 12}
print(dictA)
# {1: 123, '1': 321, '': 435, False: 12}
print(dictA[1])     # 123
print(dictA['1'])   # 321

