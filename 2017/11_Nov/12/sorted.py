strA = 'asdfghjlzxcvbqeryiy'
listA = sorted(strA)
print(type(listA))      # <class 'list'>
for i in listA:
    print(i, end=',')
    # a,b,c,d,e,f,g,h,i,j,l,q,r,s,v,x,y,y,z,

listA = sorted(strA, reverse=True)
print(type(listA))      # <class 'list'>
for i in listA:
    print(i, end=',')
    # z,y,y,x,v,s,r,q,l,j,i,h,g,f,e,d,c,b,a,

listB = [('sk4', 10), ('sk3',), ('sk3', 14), ('sk2', 14), ('sk3', 13)]
listC = sorted(listB)
print(listC)
# [('sk2', 14), ('sk3',), ('sk3', 13), ('sk3', 14), ('sk4', 10)]
# 元组 先排第一个 ，相同往下走

temp = None
for i in listC:
    if not temp:
        temp = i
    else:
        print(i > temp, end=',')
        # True,True,True,True,


def my_sort(item):
    if len(item) < 2:
        return 0
    else:
        return item[1]

listB = [('sk4', 10), ('sk3',), ('sk3', 14), ('sk2', 14), ('sk3', 13)]
listC = sorted(listB, key=my_sort)
print(listC)
# [('sk3',), ('sk4', 10), ('sk3', 13), ('sk3', 14), ('sk2', 14)]




