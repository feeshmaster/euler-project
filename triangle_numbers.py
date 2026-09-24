import math


def t(n):
    return n * (n + 1) // 2


def count_facts(num):
    count = 0
    root = math.isqrt(num)
    for n in range(1, root + 1):
        if num % n == 0:
            count += 2
            if n * n == num:
                count -= 1  
    return count


target = 500
i = 0
while True:
    i += 1
    num = t(i)
    if count_facts(num) >= 500:
        break
print(num)