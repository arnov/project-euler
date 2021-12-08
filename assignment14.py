def collatz(n, seq=None):
    if not seq:
        seq = []

    seq.append(n)

    if n == 1:
        return seq

    if n % 2 == 0:
        return collatz(n/2, seq)
    else:
        return collatz(n*3+1, seq)


max_len = 0
max_ind = None
for i in range(1, 1_000_000):
    l = len(collatz(i))

    if l > max_len:
        max_len = l
        max_ind = i

        print(f'Max start: {i}')
        print(f'Max length: {l}')
