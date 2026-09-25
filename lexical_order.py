import math
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



def next_perm(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i < 0:
        return
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1 :] = reversed(nums[i + 1 :])
    return nums

new = digits
for i in range(999999):
    new = next_perm(new)
print(new)
