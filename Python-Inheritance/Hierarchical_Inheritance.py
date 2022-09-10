class Parent:
    def parentMethod(self):
        print("parent method feature")


class Child1(Parent):
    def child1Method(self):
        print("child-1 method feature")


class Child2(Parent):
    def child2Method(self):
        print("child-2 method feature")


c = Child2()
c.parentMethod()
