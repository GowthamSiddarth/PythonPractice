"""
Take a list and write a program that prints out all the factors of the number.
"""


def getDivisorsOfNum(num):
    return [x for x in list(range(1, int(num / 2) + 1)) + [num] if 0 == num % x]


num = int(input().strip())
res = getDivisorsOfNum(num)
print(res)
