place = 1
pmax = 1000000
sums = 1
n = 0

for i in range(1, 1000000):
    l = len(str(i))
    n += l
    if (place > pmax):
        break
    while n >= place and place <= pmax:
        index = l - 1 - (n - place)
        sums *= int(str(i)[index])
        place *= 10
        
print(sums)
