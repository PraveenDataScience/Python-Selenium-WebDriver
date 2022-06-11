def deco_list(fun):
    def inner(list_of_tuples):
        return [fun(val[0],val[1]) for val in list_of_tuples]
    return inner

@deco_list
def addTuples(a,b):
    return a+b

print(addTuples([(1,4),(4,5),(3,3)]))
