""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 00-04-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Validate Email Adress with a filter
#problem link:

import re
regexp='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regex="^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"

def fun(s):# return True if s is a valid email, else return False
    '''''''''
    l = len(s)
    dot = s.find(".")  # return . position
    #print(dot)
    at = s.find("@")
    a = 0
    for i in range(0, at):  # count alphabet
        if ((s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z')):
            a = a + 1

    if (dot > 0 and (dot - at) > 0 and a > 0 and (dot + 1) < l):
        return True
    else:
        return False'''''''''
    if (re.search(regex, s)):
        return True
    else:
        return False





def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)