import random
print('猜猜0~10的数字，你有三次机会')
randomNum = random.randint(0, 10)
for i in range(3):
    num = int(input('请输入您的第' + str(i+1) + '次答案：' ))
    if num == randomNum:
        print('恭喜你！🎉🎉🎉 答对啦！！！')
        print('答对了也没奖励，游戏结束！')
        print('Game over')
        break
    if i != 2:
        if num < randomNum:
            print('您的答案小了，真的答案比较大哦')
        else:
            print('您的答案大了，真的答案比较小哦')
else:
    print('不好意思三次机会用光啦，答案是' + str(randomNum) + '！下次再来挑战吧')