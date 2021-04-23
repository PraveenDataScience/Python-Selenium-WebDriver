class Over:
    def m1(self):
        print('Function first')
    def m1(self):
        print('Function second')
    def m1(self,a,b):
        self.a=a
        self.b=b
        print(a+b)

t=Over()
#t.m1()
t.m1(5,4)