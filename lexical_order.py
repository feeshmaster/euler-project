import math
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



def next_perm(nums):
    i = len(nums) - 2






"""
def next_permutation(nums):
    # 1. Find the pivot
    i = len(nums) - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i < 0:
        return False

    # 2. Find the smallest value bigger than pivot
    j = len(nums) - 1

    while nums[j] <= nums[i]:
        j -= 1

    # 3. Swap
    nums[i], nums[j] = nums[j], nums[i]

    # 4. Reverse the suffix
    nums[i + 1 :] = reversed(nums[i + 1 :])

    return nums
print(next_permutation(next_permutation(digits)))
"""
