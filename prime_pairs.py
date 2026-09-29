import math
pairs = []

def getprimes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [x for x in range(limit + 1) if sieve[x]]

primes = getprimes(1000000)
primes = [p for p in primes if p not in [1, 2, 3, 4, 5]]
for i, p in enumerate(primes):
    if len(primes)-1 != i:
      pairs.append((p, primes[i+1]))
nums= []

for pair in pairs:
    i = 0
    while True:
        s = str(i) + str(pair[0])
        if int(s) % pair[1] == 0:
            nums.append(int(s))
            break
        i +=1
print(sum(nums))