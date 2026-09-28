import math


def getprimes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

primes = getprimes(((1000**2) + (1000*1000) + 1000))

def f(n, ac, bc):
    return primes[((n**2) + (ac*n) + bc)] == True

winner = (0,0,0)

product = 0
    
for acof in range(-999, 1000):
    for bcof in range(-999, 1000):
        n = 0
        while f(n, acof, bcof):
            n += 1
        if n > winner[0]:
            winner = (n, acof, bcof)
print(winner[1] * winner[2])
