import math

num = 2 ** 1000
s = 0
for l in str(num):
  s += int(l)

print(s)