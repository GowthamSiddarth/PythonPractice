'''
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
'''


def removeDupsStrsAndSort(strings):
    return ' '.join(list(sorted(set(strings.split()))))


strings = input().strip()
res = removeDupsStrsAndSort(strings)
print(res)
