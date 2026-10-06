def get_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, limit+1):
        if sieve[i]:
            for j in range(i**2, limit+1, i):
                sieve[j] = False
    return [x for x in range(limit+1) if sieve[x]]
    
primes = set(get_primes(1000000))
c = 0
for p in list(primes):
    s = str(p)
    rot = 0
    for i in range(1, len(s)+1):
        s = s[-1:] + s[:-1]
        if int(s) in primes:
            rot += 1
    if rot == len(s):
        c += 1
            
print(c)
