import math 
winner = (1, 0) 
def findab(c, p): 
    csq = c**2 
    sols = 0
    for a in range(1, c): 
        b = math.sqrt(csq - a**2) 
        if b.is_integer(): 
            if (a+b+c) == p: 
                sols +=1
    return sols

for p in range(1, 1001): 
    sols = 0
    for c in range(p//3, p//2):
        sols += findab(c, p)
    if winner[1] < sols:
        winner = (p, sols)
print(winner)
        
