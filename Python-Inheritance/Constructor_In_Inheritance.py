class TestA:
    def __init__(self):
        print("__init__ of TestA")

    def m1A(self):
        print("Feature M1A ")

    def m2A(self):
        print("Feature M2A ")


class TestB(TestA):
    def __init__(self):
        super().__init__()
        print("__init__ of TestB")

    def m1B(self):
        print("Feature M1B ")

    def m2B(self):
        print("Feature M2B ")


b = TestB()
