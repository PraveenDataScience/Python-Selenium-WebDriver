class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def display(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)


obj2=Student("Labs","Python")
obj2.display()
obj1=Person("VDS","TECH")
obj1.display()

