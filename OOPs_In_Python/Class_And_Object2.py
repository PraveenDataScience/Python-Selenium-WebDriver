class Student:
    """This class is for intro to Class & Object and reference variable by VDS TECH LABS"""

    def __init__(self,name,rollNo,marks):
        """Init methods behave like a constructor, whenever we are going to
        create Object of this class,this __init__() method will execute.
        """
        self.name = name
        self.rollNo = rollNo
        self.marks = marks

    def talk(self):
        """This is normal methods that will tell you student details"""
        print('My Name is : ', self.name)
        print("My roll num is : ", self.rollNo)
        print("My marks are: ", self.marks)


# Object creation in Python:
s1 = Student('VDS',102,91)
'''This is Object of class Student with reference variable s,
With reference variable s, we can call instance variable & methods.
'''
s2 = Student('VDS TECH',103,93)
s1.talk()
s2.talk()
