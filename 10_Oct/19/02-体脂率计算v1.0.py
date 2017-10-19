
sex = input("请输入性别(0代表女,其他代表男)：")
if sex == '0':
    sex = '女'
else:
    sex = '男'
print("性别：%s" % sex)
print(1 if sex == '男' else 0)

age = input("请输入年龄(整数)：")
age = float(age)
print("年龄：%f" % age)

tall = input("请输入身高(单位/m)：")
tall = float(tall)
print("身高：%f" % tall)

weight = input("请输入体重(单位/kg)：")
weight = float(weight)
print("体重：%f" % weight)

# 计算
BMI = weight / tall
res = 1.2 * BMI + 0.23 * age - 5.4 - 10.8 * (1 if sex == '男' else 0)

txtList = ['体脂率低', '体脂率正常', '体脂率高']
scope = {
    '男': (0.15, 0.18),
    '女': (0.25, 0.28)
}

if res < scope[sex][0]:
    resText = txtList[0]
elif res > scope[sex][1]:
    resText = txtList[2]
else:
    resText = txtList[1]
# 注意点 format
print('你的体脂率是：{0}%，正常范围是：{1}%~{2}%，你的{3}'.format(res, scope[sex][0] * 100, scope[sex][1] * 100, resText))
print('你的体脂率是：%.2f%%，正常范围是：%d%%~%d%%，你的%s' % (res, scope[sex][0] * 100, scope[sex][1] * 100, resText))
