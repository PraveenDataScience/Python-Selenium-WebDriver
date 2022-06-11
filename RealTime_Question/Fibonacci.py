def fibo():
    n=int(input("Enter number: "))
    a,b=0,1
    print(a,b, end=" ")
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c

fibo()