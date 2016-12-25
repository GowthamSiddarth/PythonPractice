'''
Write a program that accepts line as input and prints the lines after making all words in the sentence capitalized.
'''


def capitalizeSentence(sentence):
    return ' '.join([word.capitalize() for word in sentence.split()])


sentence = input().strip()
res = capitalizeSentence(sentence)
print(res)
