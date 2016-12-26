'''
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and
the values are square of keys.
'''


def generateCustomDict(low, high):
    return {x: x ** 2 for x in range(low, high + 1)}


low, high = tuple(map(int, input().strip().split()))
res = generateCustomDict(low, high)
print(res)
