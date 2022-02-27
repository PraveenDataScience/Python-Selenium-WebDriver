class Parent():
    pass

class b(Parent):
    pass
print(issubclass(b,Parent)) #true
print(issubclass(Parent,b)) #False

obj1=b()
obj2=Parent()
print("=======")
print(isinstance(obj2,b)) #False
print(isinstance(obj2,Parent)) #True