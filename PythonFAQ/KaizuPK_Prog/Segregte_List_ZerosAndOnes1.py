L=[0,0,1,0,1,0,0,1,1,1,0,1,0]

def segregate(list1):   
    sl=([x for x in list1 if x==0]+[x for x in list1 if x==1]+[x for x in list1 if x==2])
    print(sl)


segregate(L)