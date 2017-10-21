import random as ran

# random() => [0,1)
print(ran.random())

# choice() 随机选一个
print(ran.choice([1, 3, 5]))    # List
print(ran.choice((1, 3, 5)))    # Tuple
# print(ran.choice({'a': 123, 'b': 456}))   # 报错

# randomint(x, y) => [x,y] 随机整数
print(ran.randint(1, 8))    # 7

# uniform(x, y) => [x,y] 随机 小数
print(ran.uniform(1, 1))    # 1.0

# randrange(start, stop=None, step=1)   随机整数 [start, stop)
print(ran.randrange(100))   # [0, 100)
print(ran.randrange(1))   # [0, 1)
print(ran.randrange(100, 107, step=2))
print(ran.randrange(100, stop=400, step=2))
