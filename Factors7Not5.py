'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between low and high (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''


def get7FactorsNot5(low, high):
    return [i for i in range(low, high + 1) if (i % 7 == 0) and (i % 5 != 0)]


(low, high) = tuple(map(int, input().split()))
res = get7FactorsNot5(low, high)
print(res)
