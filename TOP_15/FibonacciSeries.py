# Print Fibonacci Series:

def f(n):
    if n==0: return 0
    elif n==1: return 1
    else: return f(n-1)+f(n-2)

for i in range(0,10):
    print(f(i),end=" ")

#2nd way:
print("\n=========================")

def fibo(n):
    #n=int(input("Enter num:"))
    a=0
    b=1
    print(a,b,end=' ')
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

fibo(10)