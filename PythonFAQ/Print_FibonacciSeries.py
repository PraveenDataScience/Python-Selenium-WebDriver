# 0 1 1 2 3 5 8
def fibo(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

fibo(8)

print("\n========================")

# 2nd Way:
def fun(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fun(x-1)+fun(x-2)

for i in range(0,8):
    print(fun(i),end=" ")