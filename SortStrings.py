'''
Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
'''


def sortStrings(strings):
    return list(sorted(strings))


strings = list(map(str, input().split(',')))
res = sortStrings(strings)
print(res)
