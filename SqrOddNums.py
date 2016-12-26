'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
'''


def getSquareOfOddNums(nums):
    return [x * x for x in nums if (x & 1 == 1)]


nums = list(map(int, input().strip().split(',')))
res = getSquareOfOddNums(nums)
print(res)
