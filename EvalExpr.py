"""
Please write a program which accepts basic mathematic expression from console and print the evaluation result.
"""


def evalexpr(expr):
    return eval(expr)


expr = input().strip()
res = evalexpr(expr)
print(res)
