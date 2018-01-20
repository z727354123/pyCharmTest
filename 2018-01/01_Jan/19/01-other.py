# 访问其他模块
# import _01_公有属性 as b
# print("ohter " +  b.Animal.nameA)
# from _01_公有属性 import Dog as dd
# print("Dog " + dd.nameA)


# import _02_protected as b
# print("ohter " +  b.Animal._nameA)
# from _02_protected import *
# print("Dog " + _name)   # 这个 不能 打印
# NameError: name '_name' is not defined
# from _02_protected import _name
# print("Dog " + _name)



from _03_private import *
# print("Dog " + __name)
# 这个 不能 打印，除非 __all__ = ["__name"]
from _03_private import __name
print("Dog " + __name)







