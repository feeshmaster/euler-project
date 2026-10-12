import math
def get_primes(l):
    s = [True] * (l+1)
    s[0] = s[1] = False
    for i in range(2, int(math.sqrt(l))+1):
        if s[i]:
            for j in range(i*i, l+1, i):
                s[j] = False
    return [x for x in range(2, l+1) if s[x]]
primes = set(get_primes(10000000))

def check(num):
    s = str(num)
    n = len(s)
    string = ''.join([str(x) for x in range(1, n+1)])
    if set(s) == set(string):
        return True
    return False
winner = 0
for p in primes:
    if check(p):
        if winner < p:
            winner = p
            
print(winner)

#primes = set(get_primes(100000000))
