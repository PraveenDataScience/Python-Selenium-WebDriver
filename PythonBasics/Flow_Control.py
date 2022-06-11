a=input('Enter a=')
b=input('Enter b=')

if a>b:
    print('a is greater than b')
elif a==b:
    print('Both are equal')
elif b>a:
    print('b is grater tha a')
else:
    print('Not greater')

x=2
y=3
print("x is less than y") if x>y else print('Not greater')