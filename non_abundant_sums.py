import math


def d(n): #sum of proper divisors so you dont forget
    product = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            product += i
    return product

abundants = set()

for i in range(0, 28124):
    if i < d(i):
        abundants.add(i)

sums = [0] * 28124

for x in abundants:
    for y in abundants:
        sumofabundants = x + y
        if sumofabundants <= 28123:
            if sums[sumofabundants] == 0:
                sums[sumofabundants] = sumofabundants
total = 0
for x in range(1, len(sums)):
    if sums[x] == 0:
        total += x

print(total)
