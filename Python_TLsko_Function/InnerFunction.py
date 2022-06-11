def outer():
    print("Outer text")

    def inner():
        print("Inner text")

    inner()


outer()


def greaterOfTwos(a, b):
    if a > b:
        return a
    else:
        return b


print(greaterOfTwos(5, 6))


def greatestOfThree(a, b, c):
    return greaterOfTwos(greaterOfTwos(a, b), c)


print(greatestOfThree(8, 9, 10))
