def dec1(func1):
    def func2():
        print("Execute func2")
        func1()
        print("Executed")

    return func2


@dec1
def VDS():
    print("Good Tutorial.....")


#vdstech = dec1(VDS)
VDS()
#vdstech()
