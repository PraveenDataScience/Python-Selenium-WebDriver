a=lambda x:x%10==0
print(a(51))

li=[10,12,15,40,13,78,90,60,30,48,99]

result=list(filter(lambda x:(x%10==0),li))

print(result)