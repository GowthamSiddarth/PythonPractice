"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""
import zlib


def compressString(s):
    return zlib.compress(str.encode(s))


def decompressStrig(s):
    return str(zlib.decompress(s), 'utf-8')


s = 'hello world!hello world!hello world!hello world!'
res = compressString(s)
print(res)
res = decompressStrig(res)
print(res)
