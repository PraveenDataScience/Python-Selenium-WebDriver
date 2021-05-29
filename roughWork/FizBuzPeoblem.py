def fiz_buzz(numbers):
    for i in range(len(numbers)):
        num=numbers[i]
        if num%3==0:
            numbers[i]="Fizz"
        if num%5==0:
            numbers[i]="Buzz"
        if num%3==0 and num%5==0:
            numbers[i]="FizzBUZZ"


num1=[45,8,25,7,30]
fiz_buzz(num1)