L1 = [1,2,3,4,5]
L2 = [6,7,8]
#What is the output of below:

#L1.append(L2)  # [1,2,3,4,5,[6,7,8]]
#print(L1)
#L1.extend(L2) #[1,2,3,4,5,6,7,8]
#print(L1)
#print(L1 + L2)  # [1,2,3,4,5,6,7,8]

T = (1,2,3,4,[5,6,7,8])
#can we change value of 5 to 10 so that the output will be:
T[4][0]=10
print(T)

L = [1,2,3,4,5]
print(L[::-1])

li=[i for i in range(1,101) if i%2==0]
print(li)

li1=[1,7,4,2,5,4,2,4,8,9]
print(li1.count(4))