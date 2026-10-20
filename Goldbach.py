import math
def gp(l):
    s = [True] * (l+1)
    s[0] = s[1] = False
    for i in range(2, int(math.sqrt(l))+1):
        if s[i]:
            for j in range(i*i, l+1, i):
                s[j] = False
    return [x for x in range(2, l+1) if s[x]]
primes = gp(1000000)
def is_composite(n):
    if n <= 1:
        return False
    if n <= 3:
        return False
    
    if n%2 == 0 or n%3 == 0:
        return True
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return True
        i += 6
    return False

for i in range(4, 100000):
    found = False
    if i%2 == 0 or not is_composite(i):
        continue
    for p in primes:
        if i <= p:
            break
        for j in range(1, p):
            if p + 2*(j**2) == i:
                found = True
    if not found:
        print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
