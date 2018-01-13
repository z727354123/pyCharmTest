# 根据 文件目录 生成 dirt
import os
destPath = "src"    #目标目录
# 1. 改变目标目录
if not os.path.isdir(destPath):
    exit(0)
os.chdir(destPath)
# 2. 定义函数 读取 返回 dict
#    dict 的 value = None 是文件 = dict 是文件夹
def getList (pathName):
    # 0. 创建 dist 用于 返回
    dirList = {}
    # 1. 获取当前目录信息 list
    listDir = os.listdir(pathName)
    # 2. 遍历目录
    for fileName in listDir:
        srcName = pathName + "/" + fileName
        # 1. 判断是文件夹
        if os.path.isdir(srcName):
            # 文件夹 递归操作
            dirList[fileName] = getList(srcName)
        else:
            # 文件，赋值为 None
            dirList[fileName] = None
    return dirList

dirList = getList("../../../../../../../")

# 根据 dirt 生成 str
# │   ├ ─ ─  └ ─ ─
strList = [" ", "│", "├", "└", "─", " 文件\n", " 目录\n"]
strOne = strList[2] + (strList[4] * 2) + strList[0]     # ├──
strTwo = strList[3] + (strList[4] * 2) + strList[0]     # └──
strThree = strList[1] + (strList[0] * 3)                # │
strFour = strList[0] * 4                                #
def getStr(dictDir, startStr = ""):
    str = ""
    # 1. 遍历 dictDir
    items = dictDir.items()
    for index, tupleVal in enumerate(items):
        # 判断是字典
        # if isinstance(tupleVal[1], dict):
        #     print(tupleVal)
        # print(index, tupleVal)
        strTemp = strOne
        startTemp = strThree
        # 1. 判断是否是 最后一个
        if index == len(items) - 1:
            strTemp = strTwo
            startTemp = strFour
        # 1. 判断是否是 文件
        str += startStr + strTemp + tupleVal[0]
        if tupleVal[1] == None:
            # 文件就 直接 添加进 str
             str += strList[5]
        else:
            # 目录 也加
            str +=  strList[6]
            # 递归加
            str += getStr(tupleVal[1], startStr=startStr + startTemp )
    return str
str = getStr(dirList)


# 3. 写入文件
os.chdir("/Users/Fizz_kai/Documents/Python/02-基础")
file = open("list.txt", "w", encoding="utf=8")
file.write(str)
file.close()