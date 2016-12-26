'''
Define a function which can generate and print a tuple where the value are square of numbers between low and high
(both included).
'''


def generateCustomTuple(low, high):
    return tuple(x ** 2 for x in range(low, high + 1))


low, high = tuple(map(int, input().strip().split()))
res = generateCustomTuple(low, high)
print(res)
