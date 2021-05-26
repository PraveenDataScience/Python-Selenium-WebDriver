def fizbuzz(num):
    for i, num in enumerate(numbers):
        if num % 5 == 0 and num % 3 == 0:
            numbers[i] = "fizzbuzz"
        elif num % 3 == 0:
            numbers[i] = "fizz"
        elif num % 5 == 0:
            numbers[i] = "buzz"


fizbuzz(5)