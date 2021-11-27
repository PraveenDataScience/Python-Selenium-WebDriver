class Student:
    """This class is for intro to Class & Object and reference variable by VDS TECH LABS"""

    def __init__(self):
        """Init methods behave like a constructor, whenever we are going to
        create Object of this class,this __init__() method will execute.
        """
        self.name = 'VDS TECH LABS'
        self.rollNo = 101
        self.marks = 90

    def talk(self):
        """This is normal methods that will tell you student details"""
        print('My Name is : ', self.name)
        print("My roll num is : ", self.rollNo)
        print("My marks are: ", self.marks)


# Object creation in Python:
s = Student()
'''This is Object of class Student with reference variable s,
With reference variable s, we can call instance variable & methods.
'''
print(s.name)
print(s.marks)
print(s.rollNo)
s.talk()
print(Student.__doc__)

print(s.talk.__doc__)
print(s.__init__.__doc__)
