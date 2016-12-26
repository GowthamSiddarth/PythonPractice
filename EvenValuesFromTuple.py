'''
Write a program to generate and print another tuple whose values are even numbers
'''


def getEvenNumsFromTuple(nums):
    return tuple(x for x in nums if x % 2 == 0)


nums = list(map(int, input().strip().split(',')))
res = getEvenNumsFromTuple(nums)
print(res)
