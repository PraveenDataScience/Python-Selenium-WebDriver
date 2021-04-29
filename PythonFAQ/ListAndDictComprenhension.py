li=[4,5,9,3,8]

li1=[4,5,4,3,9,3,8]


square_list=[x**2 for x in li]
print(square_list)

dict_sq_list={x:x*x for x in li}
print(dict_sq_list)

dict_sq_list1={x:x**2 for x in range(1,5)}
print(dict_sq_list1)