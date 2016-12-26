'''
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).
'''

'''
def specialfunc(n):
    return n * 100 + 1
'''


def specialfunc(n):
    if 0 == n:
        return 1
    else:
        return specialfunc(n - 1) + 100


n = int(input().strip())
res = specialfunc(abs(n))
print(res)
