def b2(num):
    return bin(num)[2:]
def check(s):
    return s == s[::-1]
sums = 0
for i in range(1,1000000):
    if check(str(i)) and check(b2(i)):
        sums += i
        
print(sums)

    
    
