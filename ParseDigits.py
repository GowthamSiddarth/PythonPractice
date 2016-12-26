'''
Write a program which accepts a sequence of words separated by whitespace as input to print the words
composed of digits only.
'''
import re


def parseDigits(sentence):
    return re.findall('\d+', sentence)


sentence = input().strip()
res = parseDigits(sentence)
print(res)
