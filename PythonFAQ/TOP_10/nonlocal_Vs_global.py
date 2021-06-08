def func1():
    x = 5

    def func2():
        nonlocal x
        print(x)
    func2()


func1()

x = 5
def func1():
    print(x)
func1()

x = 5
def func3():
    global x
    x += 3
func3()

