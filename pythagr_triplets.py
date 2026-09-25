import math
nproduct = 1000

for a in range(math.ceil(nproduct), math.ceil(2), -1):
    for b in range(math.ceil(nproduct), a, -1):
        c = math.sqrt((a ** 2) + (b **2))

        if ((a+b+c) == 1000):
            print("wth", a, b, c)
            print(a*b*c)

