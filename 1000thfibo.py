fibs = [1, 1]

def fib(n):
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n - 1]

n = 3
while True:
    num = fib(n)
    if len(str(num)) >= 1000:
        print(n)
        break
    n += 1