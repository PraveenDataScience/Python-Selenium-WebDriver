x=lambda a,b:a+b
print(x(5,6))

def myDouble(x):
    return lambda a:a*x

double=myDouble(5)

print(double(2))
