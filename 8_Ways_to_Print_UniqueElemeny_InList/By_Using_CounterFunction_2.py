from collections import Counter

lst1=[1,4,5,2,1,4,6,3,2,4,7,8,5,2,1,4,7]
print("Before: ",lst1)

lst2=Counter(lst1).keys()
print("After: ",lst2)
print("Count of Unique Elements are: ",len(lst2))