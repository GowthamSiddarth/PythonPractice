'''
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
'''
import re


def isValidPassword(password):
    l = len(password)
    if not re.search(pattern="[a-z]", string=password):
        return False
    elif not re.search(pattern="[A-Z]", string=password):
        return False
    elif not re.search(pattern="[0-9]", string=password):
        return False
    elif not re.search(pattern="[$#@]", string=password):
        return False
    elif re.search(pattern="[^a-zA-Z0-9$#@]", string=password):
        return False
    elif 6 > l > 12:
        return False
    else:
        return True


def getValidPasswords(passwords):
    return [password for password in passwords if isValidPassword(password)]


passwords = input().strip().split(',')
res = getValidPasswords(passwords)
print(res)
