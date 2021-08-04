class Test:
    a=10
    _b=20
    __c=30
    def m1(self):
        print(Test.a)
        print(Test._b)
        print(Test.__c)

t=Test()
t.m1()
print("=========")
print(Test.a)
print(Test._b)
print(Test.__c)