class Parent1:
    def m1(self):
        print("feature - 1")

class Parent2:
    def m2(self):
        print("feature - 2")

class Child(Parent1,Parent2):
    def m3(self):
        print("Child feature")


c=Child()
c.m2()