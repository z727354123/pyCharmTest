# 1. 获取 rem.jpg 的 内容，关闭文件
fileRem = open('rem.jpeg', 'rb')
contentRem = fileRem.read()
print(contentRem)
fileRem.close()

# 2. 把 rem.jpg的一半 写在 work.png 后面
fileWork = open('work4.jpeg', 'ab')
content = contentRem[len(contentRem) // 2:]

fileWork.write(content)
fileWork.close()
