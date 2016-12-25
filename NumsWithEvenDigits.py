'''
Write a program, which will find all such numbers between low and high (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''


def isNumWithEvenDigits(num):
    while num != 0:
        if (num % 10) % 2 != 0:
            return False
        num //= 10
    return True


def getNumsWithEvenDigits(low, high):
    return [x for x in range(low, high + 1) if isNumWithEvenDigits(x)]


(low, high) = tuple(map(int, input().strip().split()))
res = getNumsWithEvenDigits(low, high)
print(res)
