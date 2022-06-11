a=int(input("First Number: "))
b=int(input("Second Number: "))
n=int(input("Number of element : "))

print(a, b, end=" ")
while n-2:
    c=a+b
    a=b
    b=c
    print(c, end=" ")
    n=n-1