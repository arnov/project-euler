import math

for i in range(0, 1000):
    for j in range(0, 1000):
        if i < j:
            s = i**2 + j**2
            sqrt = math.sqrt(s)
            if sqrt.is_integer() and sqrt > j:
                #  print('%d^2 * %d^2 = %d^2 (= %d)' % (i, j, sqrt, s))

                if sum([i, j, sqrt]) == 1000:
                    print(i*j*sqrt)
