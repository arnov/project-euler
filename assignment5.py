def evenly_divisible(n, max_divisor):
    for i in range(2, max_divisor+1):
        if n % i != 0:
            return False

    return True

for i in range(20, 3000, 10):
    if evenly_divisible(i, 10):
        print(i)
