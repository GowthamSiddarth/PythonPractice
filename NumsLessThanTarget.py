"""
Take a list and write a program that prints out all the elements of the list that are less than target.
"""

"""
def getNumsLessThan(nums, target):
    return list(filter(lambda x: x < target, nums))
"""


def getNumsLessThan(nums, target):
    return [x for x in nums if x < target]


nums = list(map(int, input().strip().split(',')))
target = int(input().strip())
res = getNumsLessThan(nums, target)
print(res)
