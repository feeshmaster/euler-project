import math

def select(n, r)->int:
    return ((math.factorial(n))/((math.factorial(r))*(math.factorial(n-r))))
count = 0   
for n in range(1, 101):
    for r in range(1, n+1):
        if select(n, r) >= 1000000:
            count += 1
print(count)
