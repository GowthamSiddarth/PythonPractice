"""
Please write a program to print the running time of execution of a code snippet.
"""
from timeit import Timer


def getExecTime(code):
    return Timer(code).timeit()


code = input().strip()
res = getExecTime(code)
print(res)
