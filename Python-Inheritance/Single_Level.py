class A:
    def faetureA1(self):
        print("feature-1 in A")

    def faetureA2(self):
        print("feature-2 in A")

class B(A):
    def faetureB1(self):
        print("feature-1 in B")

    def faetureB2(self):
        print("feature-2 in B")

a=A()
a.faetureA1()
a.faetureA2()
print("================================")
b=B()
b.faetureB2()
b.faetureB1()