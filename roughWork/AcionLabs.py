ip = "Bottle;Table;spray;Apple;Apple;BoTtle;Basket;Basket;Spray"
d=ip.split(';')
print(d)

bl=[]

for i in d:
    if i not in bl:
        bl.append(i)

print(bl)
#Output: ["äpple","basket","bottle","spray","table"]

#Prime

print("===========Prime============")
# By List Comprehension:
a=[x for x in range(2,26) if all(x%y!=0 for y in range(2,x))]
print(a)

# By List Comprehension:
b=list(set(range(2,11)) - {x for x in range(11) for y in range(2,x) if x%y!=0})
print(b)

#"Bottle;Table;spray;Apple;Apple;BoTtle;Basket;Basket;Spray"
#["äpple","basket","bottle","spray","table",]


def sort_list(str):
  list1 = str.split(';')
  print(list1)


ls="Bottle;Table;spray;Apple;Apple;BoTtle;Basket;Basket;Spray"

sort_list(ls)