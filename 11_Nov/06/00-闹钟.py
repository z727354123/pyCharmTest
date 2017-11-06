import pygame
import winsound  # 导入此模块实现声音播放功能
import time  # 导入此模块，获取当前时间

# 提示用户设置时间和分钟
my_hour = input("请输入时：")
my_minute = input("请输入分：")

file=r'D:\cloudmusic\clound.mp3'
pygame.mixer.init()


flag = 1

while flag:
    t = time.localtime()  # 当前时间的纪元值
    fmt = "%H %M"
    now = time.strftime(fmt, t)  # 将纪元值转化为包含时、分的字符串
    now = now.split(' ') #以空格切割，将时、分放入名为now的列表中

    hour = now[0]
    minute = now[1]
    time.sleep(10)
    if hour == my_hour and minute == my_minute:
        track = pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()
        flag = 0



