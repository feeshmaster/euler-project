import math
limit = 10000


def d(n):
    product = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            product += i
    return product


nums = []

for i in range(1, limit):
    nums.append((i, d(i)))

amicables = set()
for n in nums:
    for nr in nums:
        if n[1] == nr[0] and nr[1] == n[0] and n[0] != nr[0]:
            amicables.add(n[0])
            amicables.add(nr[0])
print(sum(amicables))
