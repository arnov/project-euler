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

nr_primes = 1
i = 2
while True:
    if is_prime(i):
        print('prime nr. %d: %d' % (nr_primes, i))
        if nr_primes == 10001:
            break

        nr_primes += 1
    i += 1
