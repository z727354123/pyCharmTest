#
b = 111

def test():
    b = 10
    print("outer = " + str(b))
    def test():
        global b
        b= 222;
        print("inner = " + str(b))
        print(locals(), type(locals()))
        def inner():
            # nonlocal b
            # SyntaxError: no binding for nonlocal 'b' found
            # b += 10
            print("i inner = " + str(b))
        return inner
    b += 10
    return test


print("global = " + str(b))
inner = test()
inner2 = inner()
inner2()
print("global = " + str(b))
