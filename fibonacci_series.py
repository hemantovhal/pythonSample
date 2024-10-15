def print_fibonacci_series(intNumber):
    intA, intB = 0, 1

    for _ in range(intNumber):
        print(intA)
        intA, intB = intB, intA + intB

print_fibonacci_series(10)