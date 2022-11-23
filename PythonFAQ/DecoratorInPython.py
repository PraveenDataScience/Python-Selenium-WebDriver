def sub(a, b):
    return a - b


def alwaysPositive(func):
    def inner(x, y):
        if x > y:
            return x - y
        else:
            x, y = y, x
            return x - y
    return inner


c = alwaysPositive(sub)

print(c(10, 15))
