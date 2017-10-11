
# 验证装饰器的作用原理

re = []


def register(func):
    print("running register (%s)" % func)
    re.append(func)
    return func


@register
def func1():
    print("running func1")


@register
def func2():
    print("running func2")


def func3():
    print("running func3")


if __name__ == "__main__":

    print("running main ...")
    print("register %s" % re)
    func1()
    func2()
    func3()