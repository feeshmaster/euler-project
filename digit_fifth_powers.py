
"""

nums = []

for i in range(2, 10000000):
    l = [n for n in str(i)]
    s = 0
    for n in l:
        s += int(n) ** 5
    if s == int("".join(l)):
        nums.append(int("".join(l)))
print(nums)
"""
print(sum([4150, 4151, 54748, 92727, 93084, 194979]))