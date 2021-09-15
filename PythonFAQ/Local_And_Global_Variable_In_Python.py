a=3
def add():
    global b
    b=5
    c=a+b
    print('Sum of a & b : ',c)

add()
print(b)