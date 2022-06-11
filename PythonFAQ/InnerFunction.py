def outerFun():
    print("outer finction text")

    def inner1():
        print("Inner one")

    def inner2():
        print("Inner two")

    inner1()
    inner2()


outerFun()

def compaareTwoNos(a,b):
    if a>b:
        return a
    else:
        return b

print(compaareTwoNos(10,20))

def compaareThreeNos(a,b,c):
    return compaareTwoNos(compaareTwoNos(a,b),c)

print(compaareThreeNos(999,1000,7000))

