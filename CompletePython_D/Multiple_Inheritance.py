class A:
    def m1(self):
        print("m1 in A")

class B:
    def m1(self):
        print("m1 in B")

class C:
    def m1(self):
        print("m1 in C")

class D(C,B,A):
    pass

d=D()
d.m1()