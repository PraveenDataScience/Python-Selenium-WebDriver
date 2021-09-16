# What does *args and **kwargs mean?
#* args
#** kwargs

def mult(a,b,*c):
    mul=a*b
    for num in c:
        mul=mul*num
    return mul

#print(mult(1,2,4,5,6))

def greet(**k):
    for Key, value in k.items():
        print("{} is {} ".format(Key,value))

greet(Name="VDS TECH LABS",Course="Python",age=40)
