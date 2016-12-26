'''
Write a method which can calculate square value of number
'''


def mysquare(num):
    return num ** 2


num = int(input().strip())
res = mysquare(num)
print(res)
