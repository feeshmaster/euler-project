import math

def get_primes(l):
    s = [True] * (l+1)
    s[0] = s[1] = False
    for i in range(2, int(math.sqrt(l))+1):
        if s[i]:
            for j in range(i*i, l+1, i):
                s[j] = False
                
    return [x for x in range(l+1) if s[x]]

def solve():
    ceiling = 10000
    primes = get_primes(ceiling)
    found = [False] * (ceiling+1)
    found[0] = found[1] = True
    for prime in primes:
        found[prime] = True
        for i in range(1, int(math.sqrt(ceiling-prime)/2)+1):
            n = prime + 2*(i**2)
            if n < ceiling:
                found[n] = True

    for n, works in enumerate(found):
        if not works and n % 2 == 1:
            return n
            
print(solve())
