# Prime number 50-100:

def primeNum(x,y):
         for num in range(x,y):
            if all(num%i!=0 for i in range(2,num)):
                print(num)

primeNum(50,100)

