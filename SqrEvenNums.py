def getSqrOfEvenNums(nums):
    return list(map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, nums))))


nums = list(map(int, input().strip().split(',')))
res = getSqrOfEvenNums(nums)
print(res)
