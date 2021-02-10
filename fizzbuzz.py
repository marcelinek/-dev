for a in range(1,100):
    print("Fizz" * (a % 3 == 0) + (a % 5 == 0) * "Buzz" or a, end=",")
    if a == 99:
        print("Buzz")
