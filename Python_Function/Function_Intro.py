def sum(a,b):
    c=a+b
    print(c)

sum(4,5)

def sum1(a,b):
    c=a+b
    return c
res=sum1(5,5)
print(res)

#Function may return multiple values:
def sub_add(a,b):
    x=a+b
    y=a-b
    return x,y

res1,res2=sub_add(10,8)
print(res1,res2)