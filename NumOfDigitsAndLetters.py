'''
Write a program that accepts a sentence and calculate the number of letters and digits.
'''


def getNumOfDigitsAndChars(sentence):
    numOfChars, numOfDigits = 0, 0
    for letter in sentence:
        if (letter.isdigit()):
            numOfDigits += 1
        elif (letter.isalpha()):
            numOfChars += 1
    return (numOfDigits, numOfChars)


sentence = input().strip()
res = getNumOfDigitsAndChars(sentence)
print(res)
