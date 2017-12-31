myStr = 'string'
print(myStr.endswith('ing'))        # True
print(myStr.endswith('in', 0, -1))  # True 倒数
print(myStr.endswith('in', 0, 5))   # True 5代表g，不含尾，只匹配到in，故True
print(myStr.endswith('in', 0, 6))   # False
print(myStr.endswith('ing', 3))     # True 含头
print(myStr.endswith('ing', 4))     # False 只能从 n 开始
