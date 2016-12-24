'''
Define a class which has at least two methods:
1: to get a string from console input
2: to print the string in upper case.
'''


class MyReadWrite:
    def __init__(self):
        self.buff = ''

    def write(self):
        print(self.buff.upper())

    def read(self):
        self.buff = input()


myReadWrite = MyReadWrite()
myReadWrite.read()
myReadWrite.write()
