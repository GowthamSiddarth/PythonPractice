"""
The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.
"""

'''
def getNthFibonacci(n):
    if 0 == n:
        return 0
    elif 1 == n:
        return 1
    else:
        return getNthFibonacci(n - 1) + getNthFibonacci(n - 2)
'''
import numpy


def getNthFibonacci(n):
    return (numpy.matrix('1 1; 1 0', dtype=numpy.object) ** n).item(1)


n = int(input().strip())
res = getNthFibonacci(n)
print(res)
