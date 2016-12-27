"""
Write a python script to delete all elements with even indices in the given list.
"""


def deleteEvenIndices(nums):
    return [x for (i, x) in enumerate(nums) if i % 2 != 0]


nums = list(map(int, input().strip().split(',')))
res = deleteEvenIndices(nums)
print(res)
