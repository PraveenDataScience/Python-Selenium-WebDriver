class InitDemo:
    def __init__(self,name):
        self.name=name

    def m1(self):
        print("Hi My Name is",self.name)

emp=InitDemo("VDS TECH LABS")
emp.m1()