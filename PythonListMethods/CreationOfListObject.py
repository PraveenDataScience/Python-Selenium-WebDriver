#1 Empty List
l=[]
print(l)
print(type(l))

#2: If we know the element already:
l2=[10,20,30,40,50]
print(l2)

# With Dynamic Input:
l3=eval(input("Enter list : ")) # ['Ram',3,5,6,7,8]
print(l3)
print(type(l3))

for i in l3:
    print(i)

# With list() function:
# NOTE: From list() method we can convert any squence(e.g: str/range/tuple etc.) in list
l4=list(range(1,12,3))
print(l4)
print(type(l4))

l5=list('Praveen')
print(l5)

# With split() Function:
s="Learning python is very very easy"
l6=s.split()
print(l6)