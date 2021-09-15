class Init_demo():
    def __init__(self,name):
        self.name=name

    def m1(self):
        print("I am from ",self.name)

obj=Init_demo("VDS TECH LABS")
obj.m1()