def decorator2(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello=function(arg1,arg2)
        return string_hello
    return wrapper