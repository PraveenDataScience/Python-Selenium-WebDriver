class A:
    def featA1(self):
        print("feature A1")
    def featA2(self):
        print("feature A2")
class B:
    def featB1(self):
        print("feature B1")
    def featB2(self):
        print("feature B2")

class C(A,B):
    def featC1(self):
        print("feature C1")
    def featC2(self):
        print("feature C2")

a1=A()
b1=B()
c1=C()

