# 函数作用域
def test():
    arr = []
    for i in range(1, 4):
        def myFun():
            nonlocal i
            i += 1
            print(i)
            return
        arr.append(myFun)
    print("i = " + str(i))
    return arr

arr = test()

print(arr)
arr[0]()
arr[1]()
arr[2]()

