def fibo(n):
    a,b=0,1
    while(a<n):
        yield a
        a,b=b,a+b

x=fibo(10)
for i in x:
    print(i,end=' ')