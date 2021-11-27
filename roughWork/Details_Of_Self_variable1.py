class Student:
    def __init__(self,name,marks,rollNo):
        self.name=name
        self.marks=marks
        self.rollNo=rollNo
        print(id(self))

    @staticmethod
    def m2():
        print("Static method")

    def m1(self):
        print("name of student: ",self.name)
        print("Marks of student: ",self.marks)
        print("RollNo of student: ", self.rollNo)


s1=Student('VDS',101,98)
print(id(s1))
s1.m1()
Student.m2()