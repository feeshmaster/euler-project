def get_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, limit + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return [x for x in range(limit+1) if sieve[x]]

def check(num):
    for i in range(1, len(num)):
        if int(num[i:]) not in primes:
            return False
        if int(num[:len(num)-i]) not in primes:
            return False

    return True


primes = set(get_primes(1000000))
sums = 0
c = 0
for p in primes:
    if c == 11:
        break
    if p > 10:
        s = str(p)
        if check(s):
            print(p, p in primes)
            sums += p
            c += 1
print(sums)