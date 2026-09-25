import math
product = 0

for n in str(math.factorial(100)):
    product += int(n)

print(product)