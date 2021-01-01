import math

primes = []
memoised_prime_factors = {}

def is_prime(n):
    if n in primes:
        return True

    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    primes.append(n)
    return True

def prime_factors(n):
    if n in memoised_prime_factors:
        return memoised_prime_factors[n]

    factors = set([])
    for i in range(n/2, 1, -1):
        if n % i == 0:
            if is_prime(i):
                factors.add(i)
            else:
                factors.union(prime_factors(i))

    memoised_prime_factors[n] = factors
    return factors

def highest_prime_factor(n):
    for i in range(1, int(n / 2), 2):
        if n % i == 0 and is_prime(i):
            print(i)

print(highest_prime_factor(600851475143))
