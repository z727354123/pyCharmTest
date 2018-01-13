# seek 用法
f = open('a.txt', 'r+', encoding="UTF-8")

print(f.seek(3))    #中字 = 3个字节
print(f.read(), f.write("XX"), f.tell())

print("xx tell")
import time
time.sleep(2)

f.write("222")
f.close()


