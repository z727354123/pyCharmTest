# 定义一个经典类
class Money:
    pass

# 打印类
print(Money)
xxx = Money
print(xxx.__name__)
# 创建一个对象
obj = Money()

# 打印该对象
print(obj)


obj.name = "李四"
obj.obj = obj


print(obj.obj.obj.obj.name )
