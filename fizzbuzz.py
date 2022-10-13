def x(range):
    for x in range(1, 101):
        if (x % 3 == 0 and x % 5 == 0):
            print("FizzBuzz")
        elif (x % 3 == 0):
            print("Fizz")
        elif (x % 5 == 0):
            print("Buzz")
        else:
            print(x)
    return f"for every number divisible by 3 it returns fizz, and for 5 buzz and for both fizzbuzz"


print(x(range))