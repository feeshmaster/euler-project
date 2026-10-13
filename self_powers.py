n = str(sum([p**p for p in range(1, 1001)]))
print(n[len(n)-10:])
s = 0
for p in range(1, 1001):
    s += p**p
print(s == n)