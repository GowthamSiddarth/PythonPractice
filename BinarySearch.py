"""
Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.
"""

"""
def BinarySearch(nums, key, low_i, high_i):
    if low_i > high_i:
        return -1
    mid_i = (low_i + high_i) // 2
    if key < nums[mid_i]:
        return BinarySearch(nums, key, low_i, mid_i - 1)
    else:
        return BinarySearch(nums, key, mid_i + 1, high_i)
"""


def BinarySearch(nums, key):
    low_i, high_i = 0, len(nums) - 1
    while low_i <= high_i:
        mid_i = (low_i + high_i) // 2
        if key == nums[mid_i]:
            return mid_i
        elif key < nums[mid_i]:
            high_i = mid_i - 1
        else:
            low_i = mid_i + 1
    return -1


nums = list(sorted(map(int, input().strip().split(','))))
key = int(input().strip())
# res = BinarySearch(nums, key, 0, len(nums) - 1)
res = BinarySearch(nums, key)
print(res)
