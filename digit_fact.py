import math
sums = 0
for i in range(3, 2500000):
    d = str(i)
    s = 0
    for digit in d:
        s += math.factorial(int(digit))
    if s == i:
        sums += i
        
print(sums)
        
