class A:
    def show(self):
        print("show in A")

class B(A):
    #pass
    def show(self):
        print("show in B")

b=B()
b.show()