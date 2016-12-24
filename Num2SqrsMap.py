'''
With a given integral numbers as list, write a program to generate a dictionary that contains (i, i*i) such that i is an integral
number in the list and then the program should print the dictionary.
'''


def mapNums2Sqrs(nums):
    return {i: i * i for i in nums}


nums = list(map(int, input().split()))
res = mapNums2Sqrs(nums)
print(res)
