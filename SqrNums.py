def getSqrOfNums(nums):
    return list(map(lambda x: x ** 2, nums))


nums = list(map(int, input().strip().split(',')))
res = getSqrOfNums(nums)
print(res)
