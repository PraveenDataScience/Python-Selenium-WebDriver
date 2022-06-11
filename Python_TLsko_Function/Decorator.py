def minus(a, b):
    return a - b


def alwaysPositive(func):
    def inner(a, b):
        if a > b:
            return a-b
            #print(a - b)

        else:
            pass
            #print("a is greater than b")

    return inner


m = alwaysPositive(minus)
print(m(10, 6))

#==============================
def sub(a, b):
    return a - b


def alwaysPositive1(fumc):
    def inner(x, y):
        if x > y:
            return x - y
        else:
            x, y = y, x
            return x-y

    return inner


a = alwaysPositive1(sub)
print(a(0, 4))

