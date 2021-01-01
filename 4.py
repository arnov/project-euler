def palindrome(x):
    x = str(x)

    if x == x[::-1]:
        return True
    else:
        return False

palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        x = i * j

        if palindrome(x):
            palindromes.append(x)
            print("%d x %d = %d" % (i, j, x))

print('Max:', max(palindromes))
