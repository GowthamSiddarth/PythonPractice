'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
'''


def getNumOfUpperAndLower(sentence):
    numOfUpper, numOfLower = 0, 0
    for x in sentence:
        if x.isupper():
            numOfUpper += 1
        elif x.islower():
            numOfLower += 1
    return (numOfUpper, numOfLower)


sentence = input().strip()
res = getNumOfUpperAndLower(sentence)
print(res)
