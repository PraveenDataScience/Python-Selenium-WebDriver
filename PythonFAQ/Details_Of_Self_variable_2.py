class Student:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo

    def m1(self):
        print("Name of Student", self.name)
        print("RollNo of Student", self.rollNo)

    @classmethod
    def m2(cls):
        print("This is class method")

    @staticmethod
    def sum(a, b):
        return a + b


s1 = Student("VDS", 103)
s1.m1()
s1.m2()
print(s1.sum(10, 20))
Student.m2()
print(Student.sum(5, 4))
