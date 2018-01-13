# 根据 文件目录 生成 dirt
import os

os.chdir("/Users/Fizz_kai/Documents/Python/02-基础")
file = open("list.txt", "w", encoding="utf=8")

destPath = "/Users/Fizz_kai"    #目标目录
# 1. 改变目标目录
if not os.path.isdir(destPath):
    exit(0)
os.chdir(destPath)
# 2. 定义函数 读取 返回 dict
#    dict 的 value = None 是文件 = dict 是文件夹
def getList (pathName, num = 1):
    # 1. 获取当前目录信息 list
    listDir = os.listdir(pathName)
    # 2. 遍历目录
    for fileName in listDir:
        srcName = pathName + "/" + fileName
        file.write("  " * num + fileName)
        # 1. 判断是文件夹
        if os.path.isdir(srcName):
            # 文件夹 递归操作
            file.write(" 文件夹\n")
            getList(srcName, num + 1)
        else:
            file.write("\n")
dirList = getList("./")

# 根据 dirt 生成 str
file.close()