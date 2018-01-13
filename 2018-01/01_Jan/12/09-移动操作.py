#
import os
import shutil
shutil.move("src2/abcd.txt", "./qq.txt")

# // 不会 创建新目录
# // 若最后一个目录不存在，直接 变成目录名文件