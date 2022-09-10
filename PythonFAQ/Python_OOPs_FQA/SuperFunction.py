class A:
    def __init__(self):
        print("init in A")
    def m1(self):
        print("feature m1")

    def m2(self):
        print("feature m2")

class B(A):
    def __init__(self):
        super().__init__()
        print("init of B")
    def m3(self):

        print("feature m3")
        super().m1()

    def m4(self):
        print("feature m4")

b=B()
b.m3()