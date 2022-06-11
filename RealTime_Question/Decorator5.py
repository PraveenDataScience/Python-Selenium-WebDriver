def decoratorFun(fun):
    def inner(list_of_tuples):
        return [fun(val[0],val[1]) for val in list_of_tuples]
    return inner

@decoratorFun
def add(a,b):
    return a+b


print(add([(4,5),(8,5),(9,9)]))
