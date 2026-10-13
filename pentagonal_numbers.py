import math

def p(n):
    return int(n * ((3*n)-1)/2)
def qf(a, b, c):
    return (((-b) + math.sqrt(b**2 - (4*a*c)))/(2*a), ((-b) - math.sqrt(b**2 - (4*a*c)))/(2*a))
res = qf(3, -1, -184)
if res[0].is_integer():
    print(res[0])
elif res[1].is_integer():
    print(res[1])


ex = 10
Loop = True
while Loop:
    for n in range(1, 10*ex):
        if Loop == False:
            break
        for n2 in range(1, 10*ex):
            pn1 = p(n)
            pn2 = p(n2)
            res = qf(3,-1, -2*(pn1 + pn2))
            if not res[0].is_integer():
                continue
            elif not res[1].is_integer():
                continue
            res = qf(3,-1, -2*(abs(pn1 - pn2)))
            if not res[0].is_integer():
                continue
            elif not res[1].is_integer():
                continue
            print(n, n2, pn1, pn2)
            Loop = False
            break
    ex += 1