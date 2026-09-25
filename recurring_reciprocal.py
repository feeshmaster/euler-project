import math

dlim = 1000

def getprimes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [x for x in range(limit + 1) if sieve[x]]

primes = getprimes(dlim)

arr = []

for d in range(1, 1000):
    num = 1/d
    if len(str(num)) >= 1:
        arr.append(num)


cnt = 0

for ch in arr:
    cnt += 1
    if len(str(ch)[2:]) == 16:
        if str(ch)[2:10] == str(ch)[10:18]:
            print(f'{cnt}) {ch} --> {len(str(ch)[2:])}')




# read to understand this, holyyyy its hard

def find_recurring_cycle(numerator: int, denominator: int) -> str:
    solution = ""
    remainder_list = []
    
    while numerator % denominator == numerator:
        numerator = numerator * 10
        
        if numerator % denominator > 0:
            quotient = numerator // denominator
            if numerator % denominator in remainder_list:
                break
            remainder_list.append(numerator % denominator)
            solution = solution + str(quotient)
            numerator = numerator - denominator * quotient
        
    return solution

maximum_length = 0
final_solution = 0

for i in range(1, 1000):
    solution_string = find_recurring_cycle(1, i)
    if maximum_length < len(solution_string):
        maximum_length = len(solution_string)
        final_solution = i

print(f"The number of digits in the cycle of {final_solution} is = {maximum_length}")