'''
Write a program which can map() to make a list whose elements are square of elements
'''


def getSqrOfNums(nums):
    return list(map(lambda x: x ** 2, nums))


nums = list(map(int, input().strip().split(',')))
res = getSqrOfNums(nums)
print(res)
