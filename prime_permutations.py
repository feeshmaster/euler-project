import math



def gp(l):
  s = [True] * (l + 1)
  s[0] = s[1] = False
  for i in range(2, int(math.sqrt(l)) + 1):
    if s[i]:
      for j in range(i * i, l + 1, i):
        s[j] = False
  return [x for x in range(2, l + 1) if s[x]]



primes = [p for p in gp(9999) if len(str(p)) == 4]
prime_set = set(primes)


def is_permutation(n1, n2):
  return sorted(str(n1)) == sorted(str(n2))



found = []
for i in range(len(primes)):
  for j in range(i + 1, len(primes)):
    p1 = primes[i]
    p2 = primes[j]
    diff = p2 - p1
    p3 = p2 + diff

    if p3 in prime_set:
      if is_permutation(p1, p2) and is_permutation(p1, p3):
        seq = [p1, p2, p3]
        if seq not in found:
          found.append(seq)
          print(seq)
