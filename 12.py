from math import sqrt


def triangle(n):
    return sum(range(n+1))


def factors(n):
    f = set()
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            f.add(i)
            f.add(int(n/i))
    f.add(n)

    return f


def main():
    max_len = 0
    for i in range(1000_000):
        t = triangle(i)
        f = len(factors(t))

        if f > max_len:
            print(f'i: {i}')
            print(f'triangle: {t}')
            print(f'nr. factors: {f}')

            max_len = f

        if f > 500:
            break


if __name__ == '__main__':
    main()
