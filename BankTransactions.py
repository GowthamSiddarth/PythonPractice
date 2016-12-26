'''
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
'''


def getNetAmount():
    d, w = 0, 0
    while True:
        ip = input().strip()
        if len(ip) > 0:
            t, m = ip[0], int(ip[2:])
            if t == 'D':
                d += m
            elif t == 'W':
                w += m
        else:
            break
    return d - w


res = getNetAmount()
print(res)
