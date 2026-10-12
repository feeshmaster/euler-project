import math
words = []
count = 0
with open("words.txt","r") as f:
    words = f.read().replace('"', '').split(",")
def q(a, b, c):
    return (((-b)+math.sqrt(b**2 + (4*a*c)))/(2*a), ((-b)-math.sqrt(b**2 + (4*a*c)))/(2*a))
for word in words:
    s = 0
    for l in word:
        s += ord(l) - 64
    res = q(1,1,s*2)
    if res[0].is_integer() or res[1].is_integer():
        count +=1
print(count)
