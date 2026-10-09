import math


winner = 0
for n in range(2, 8):
    for i in range(1, 9999):
        s = ""
        for j in range(1, n+1):
            s += str(n * i)
        if len(s) == 9 and set(s) == set("123456789"):
            if int(s) > winner:
                print(1)
                winner = int(s)

print(winner)
