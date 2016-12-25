'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
'''


def gen2DArray(rows, cols):
    return [[i * j for j in range(cols)] for i in range(rows)]


(x, y) = tuple(map(int, input().split()))
res = gen2DArray(rows=x, cols=y)
print(res)
