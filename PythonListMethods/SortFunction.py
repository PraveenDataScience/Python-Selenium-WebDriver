cars=['Ford','BMW','Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sort with function:
def myFun(e):
    return len(e)

name=['Priya','Praveen','MAA','BAAP','RAM']

name.sort(key=myFun)
print(name)

name.sort(key=myFun,reverse=True)
print(name)

# Sort of List of dictionaries with function:
def myFun1(e):
    return e['Year']
l1=[{'car':'BMW','Year':2016},{'car':'TOYOTA','Year':2019},{'car':'VM','Year':2014}]

l1.sort(key=myFun1)
print(l1)

l1.sort(key=myFun1,reverse=True)
print(l1)