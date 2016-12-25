'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
'''


def sumOfa(a):
    return int('%s' % a) + int('%s%s' % (a, a)) + int('%s%s%s' % (a, a, a)) + int('%s%s%s%s' % (a, a, a, a))


a = int(input().strip())
res = sumOfa(a)
print(res)
