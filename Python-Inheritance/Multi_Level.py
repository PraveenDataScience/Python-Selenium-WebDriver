class A:
    def m1A(self):
        print("A-1")

    def m2A(self):
        print("A-2")


class B(A):
    def m1B(self):
        print("B-1")

    def m2B(self):
        print("B-2")


class C(B):
    def m1C(self):
        print("B-1")

    def m2C(self):
        print("B-2")


# Now we can call all classes of mothod
c = C()
