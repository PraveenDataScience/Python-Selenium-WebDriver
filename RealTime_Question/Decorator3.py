def decorator_list(fun):
    def inner(list_of_tuples):
        return [fun(val[0],val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def add_together(a,b):
    return a+b

print(add_together([(1,3),(4,5),(8,9),(9,9)]))