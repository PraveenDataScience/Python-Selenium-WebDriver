class A:
    def fun1(self):
        print("function A1")

class B(A):
    def fun2(self):
        print("function B2")

class C(A):
    def fun3(self):
        print("function C3")

class D(A,B,C):
    def fun4(self):
        print("function D4")

d=D()
