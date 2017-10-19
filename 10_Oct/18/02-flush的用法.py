from time import sleep
# print 立即输出的是查看有没有 换行

print('had output', end='')
print('out \n had output', end='')
print('no out put', end='', flush=True)
sleep(2)
print('no out put', end='')
print('nXXXXX', end='', flush=True)
print('no out put', end='')
sleep(2)


