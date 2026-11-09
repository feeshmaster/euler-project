import math

def p(n):
    return int(n * ((3*n)-1)/2)
def qf(a, b, c):
    return max((((-b) + math.sqrt(b**2 - (4*a*c)))/(2*a), ((-b) - math.sqrt(b**2 - (4*a*c)))/(2*a)))
res = qf(3, -1, -184)

def solve():
    pentagonals = set()
    n = 1
    while True:
        p1 = p(n)
        for p2 in pentagonals:
            d = abs(p1 - p2)
            s = p1 + p2
            qs = qf(3, -1, -2*(s))
            qd = qf(3, -1, -2*(d))
            if qs.is_integer() and qd.is_integer():
                print(d)
                return
        pentagonals.add(p1)
        n += 1
        
solve()
