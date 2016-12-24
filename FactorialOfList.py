'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
'''
from math import factorial


def getListOfFactorials(lst):
    return list(map(factorial, lst))


nums = list(map(int, input().split()))
factNums = getListOfFactorials(nums)
print(factNums)
