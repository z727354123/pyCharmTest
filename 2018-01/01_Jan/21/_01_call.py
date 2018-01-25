# call 方法
class Person:
    # def __call__(self, *args, **kwargs):
    #     print(self.__class__.__name__, args, kwargs);
    pass

p = Person()
# p('arg1', 'arg2', key1='value', key2='value')


# def test(p_type, p_color):
#     print( "一个画笔:%s，颜色：%s" % (p_type, p_color) )
#
#
# import functools
# func = functools.partial(test, "钢笔")
#
# func("红色")
# func("绿色")
# func("红色")

# __call__ 应用场景
class PenFactory:
    def __init__(self, p_type):
        self.p_type = p_type
    def __call__(self, p_color):
        self.p_color = p_color
        print("创建了一个%s这个类型的画笔，它的颜色是：%s"%(self.p_type, self.p_color))

qianbiF = PenFactory("铅笔")

qianbiF("红色")
qianbiF("黄色")
qianbiF("粉色")