weekdays1 = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays1)
print(listAsString)

#========================================================

weekdays2 = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = tuple(weekdays2)
print(listAsTuple)

#========================================================
weekdays3 = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
listAsSet = set(weekdays3)
print(listAsSet)

#=========================================================
weekdays4 = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(weekdays4.count('mon'))

weekdays5 = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[x,weekdays5.count(x)] for x in set(weekdays5)])

#============================================================
names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-3])

#=======================================================
# Write a Python Program to Check Common Letters in Two Input Strings?
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)