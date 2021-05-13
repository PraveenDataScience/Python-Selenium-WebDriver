# Sort the List:

l=[100,200,4,50,8.5,99,8,3,7,4,55,66]
l.sort(reverse=True)
print(l)

def myfunc(n):
  return abs(n - 50)

l.sort(key=myfunc)
print(l)