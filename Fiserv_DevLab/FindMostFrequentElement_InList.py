l1=[4,2,4,5,8,9,6,3,2,5,4,1,2,5,4,1,2,55,4,4,4,4]

print(max(set(l1),key=l1.count))

print("=============Using mode=================")
import statistics
from statistics import mode

def frequent_element(l):
    return mode(l)


print(frequent_element(l1))