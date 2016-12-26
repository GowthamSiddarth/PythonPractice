def getEvenNumsFromList(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


nums = list(map(int, input().strip().split(',')))
res = getEvenNumsFromList(nums)
print(res)
