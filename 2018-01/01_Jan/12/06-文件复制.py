# 打开文件
src = open("a.txt", "r", encoding="utf-8")
dest = open("b.txt", "w", encoding="GBK")

# 读取 写入
content = src.read()
dest.write(content)

# 关闭
src.close()
dest.close()

