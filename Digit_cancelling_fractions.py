


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a%b
    return a

fracs = []
for j in range (10, 100):
    for i in range(10, j):
        d1 = str (i)
        d2 = str(j)
        for d in d1:
            if d in d2:
                D1 = int(d1.replace(d, "", 1))
                D2 = int(d2.replace(d, "", 1))
                if D1 == 0 or D2 == 0 or d == '0':
                    continue
                if D1 / D2 == i / j:
                    fracs.append((i,j))
                    print (f"{D1}/{D2} from {i}/{j}")
result = (1,1)
for f in fracs:
    result = (result[0] * f[0], result[1] * f[1])
cd = gcd(result[0], result[1])
fd = result[1] // cd
print(fd)

