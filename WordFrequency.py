'''
Write a program to compute the frequency of the words from the input. The output should output after
sorting the key alphanumerically.
'''


def getFrequencyOfWords(sentence):
    frequencies = {}
    for word in sentence.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return sorted(frequencies.items())


sentence = input().strip()
res = getFrequencyOfWords(sentence)
print(res)
