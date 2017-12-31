print('a' and False)    # False
print('a' and True)     # True
print(True and "a")     # a
print('' and False)     # ''
print('' or 'dis')     # 'dis'
print(True or "a")      # True
print('a' or True)      # a
# 由此可见，and 优先传开头的 假值，或者 直接最后一个值
# 由此可见，or 优先传开头的 真值，或者 直接最后一个值

print(not '')       # True
print(not 'aa')     # False
print(not 0)        # True
print(not 123)      # False
print(not -1)      # False