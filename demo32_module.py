# encoding=utf-8
def foo(x, y):
    return "[foo]:result=%s" % str(x + y)


def bar(x, y):
    return "[bar]:result=%s" % str(x * y)


def Dinner(meat, veg):
    return "Meat :%s Vegetable : %s" % (meat, veg)


# 在此FILE中才會執行，若為Import的話不會執行這段
if __name__ == '__main__':
    print foo(1, 2)
    print bar(3, 4)
    print Dinner("Chicken", "Tomatos")
else :
    print '你真的有IMPORT到喔!!!!!'
