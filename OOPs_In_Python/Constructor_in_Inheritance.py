class A:
    def __init__(self):
        print("init in A")

    def featA1(self):
        print("feature A1")
    def featA2(self):
        print("feature A2")
class B(A):
    def __init__(self):
        super().__init__()
        print("init in B")
    def featB1(self):
        print("feature B1")
    def featB2(self):
        print("feature B2")

#a=A()
b=B()