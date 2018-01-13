# │   ├ ─ ─  └ ─ ─
# 1. 该变目标目录
import os
os.chdir("src")

# 2. 获取文件列表
fileList = os.listdir()

# 3. 获取文件列表，分类，移动
# 3.1 创建dict 存储 分类信息
fileDict = {}
# 3.2 遍历文件列表,记录，移动
for val in fileList:
    index = val.rfind(".", )   # rfind = 从右边找
    if index == -1:  # 文件夹跳过



        continue
    dirStr = val[index + 1:] # 文件夹名
    arr = fileDict.setdefault(dirStr, [])  # 获取数组
    arr.append(val) # 添加进数组
    # 创建目录
    if not os.path.exists(dirStr):  # 判断文件夹 是否存在
        os.mkdir(dirStr) #不存在 就创建
    # 移动操作
    os.rename(val, dirStr + "/" + val)

# 4. 根据dict 生成txt 文本
str = "生成的清单为：\n"
for index, key in enumerate(fileDict):
    if index == len(fileDict) - 1:
        str += "┗━ "    # 最后一个父 没有下一个
    else:
        str += "┣━ "
    str += key + "\n"
    # 二级目录
    for index2, val in enumerate(fileDict[key]):
        if index == len(fileDict) - 1:
            str += "    "   # 最后一个父 没有下一个
        else:
            str += "┃   "
        if index2 == len(fileDict[key]) - 1:
            str += "┗━ "    # 最后一个父子 没有下一个
        else:
            str += "┣━ "
        str += val + "\n"   # 换行

# 5. 写入操作
listTxt = open("list.txt", "w", encoding="UTF-8")
listTxt.write(str)  # 默认是 'ascii' ASCII 不支持中文
listTxt.close()



# 0. 测试
# dict = {"name":"lisi", "age": 18}
#
#
# items = dict.items()
# items = [1,2,3,4,5,9]
# enum = enumerate(items)
#
# for index, val in enum:
#     print(index, val)
#     print(len(items))