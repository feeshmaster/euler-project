def get_primes(l):
    s = [True] * (l+1)
    s[0] = s[1] = False
    for i in range(2, l+1):
        if s[i]:
            for j in range(i*i, l+1, i):
                s[j] = False
    return [x for x in range(l+1) if s[x]]

primes = get_primes(1000100)
sums = 0
for index, p1 in enumerate(primes):
    if p1 < 5:
        continue
    if p1 > 1000000:
        break
    p2 = primes[index + 1]
    
    co = 10 ** len(str(p1))
    i = pow(co, -1, p2)
    n = (i * -p1) % p2
    sums += n*co + p1
    
print(sums)
