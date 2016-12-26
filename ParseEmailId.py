'''
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
company name and username of a given email address. Both user names and company names are composed of letters only.
'''


def getUsername(email):
    return email[:email.index('@')]


def getDomainname(email):
    return email[email.index('@') + 1:]


email = input().strip()
username = getUsername(email)
domainname = getDomainname(email)
print(username, domainname)
