import numpy as np

L1=[2,3,6,9,8,5,2,3,6,9,8,5]
print("Before: ",L1)
L2=np.unique(L1)
print("After: ",L2)
print("No Of Unique element: ",len(L2))