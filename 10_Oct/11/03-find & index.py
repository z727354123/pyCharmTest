myStr = 'Python'
print(myStr.find('Py'))     # 0
print(myStr.find('py'))     # -1 区分大小写
print(myStr.index('Py'))    # 0
print(myStr.index('py'))    # ValueError: substring not found

