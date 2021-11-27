class Emp:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid
        print(id(self))

    def e1(self):
        print("Name of Emp: ", self.name)
        print("Emp id is : ", self.empid)


e = Emp('VDS', 100)
print(id(e))
e.e1()
