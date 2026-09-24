


def odd(n):
    return (3*n)+1
    
def even(n):
    return n/2

def collatz(start):
    chain = 0
    num = start
    while True:
        if num == 1:
            chain += 1
            break
        if num % 2 == 0:
            num = even(num)
        else:
            num = odd(num)
        chain += 1
    return (start, chain)

limit = 999999
max_collatz = (0, 0)
for i in range(2, limit):
    if i % 10000 == 0:
        print(i)
    num = collatz(i)
    if num[1] > max_collatz[1]:
        max_collatz = num
print(max_collatz)
