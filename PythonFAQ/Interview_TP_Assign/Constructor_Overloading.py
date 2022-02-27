# Note: The constructor overloading is not allowed in Python.
class A:
    def __init__(self):
        print("The First Constructor")
    def __init__(self):
        print("The second contructor")

st = A()