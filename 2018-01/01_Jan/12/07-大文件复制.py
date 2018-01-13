# 大文件复制
src = open("a.txt", "r", encoding="utf-8")
dest = open("b.txt", "w", encoding="utf-8")

import time
# 分段复制
while True:
    time.sleep(1)
    content = src.read(128)
    if len(content) == 0:
        break
    dest.write(content)
    dest.flush()

# 关闭文件
src.close()
dest.close()

