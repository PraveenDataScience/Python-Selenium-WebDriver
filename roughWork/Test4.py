l1=[10,45,20,12,70,80,90,30,56]

a=lambda x :x%10==0
print(a(51))

num_10=list(filter(lambda x:(x%15==0),l1))
print(num_10)
