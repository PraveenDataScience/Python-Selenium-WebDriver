str='example'
print  (str.center(2,'*'))


class Assign:
    def __init__(self, value=0):
        self.__value = value


obj1 = Assign(2)
obj2 = Assign(2)
print(id(obj1) == id(obj2))
str1 = 'Good'
str2 = 'Good'
print(id(str1) == id(str2))

print (R'Tech\nBeamers')

str='Hello World'
print  (str.replace('l','n',2))


str='Tech Beamers'
str[4]='-'
print (str)