# username changes

## run time error
# def possibleChanges(usernames):
#     # Write your code here
#     result=[]
#     for uname in usernames:
#         flag=0
#         for i in range(len(uname)):
#             # j=i+1
#             for j in range(i+1,len(uname)):
#                 if ord(uname[i].lower())>ord(uname[j].lower()):
#                     # result.append('YES')
#                     flag=1
#                     break
#             if flag==1:
#                 break
#         if flag==1:
#             result.append('YES')
#         elif flag==0:
#             result.append('NO')
#     return result

import functools

## No run time error
def possibleChanges(usernames):
    # Write your code here
    result = []
    for uname in usernames:
        res = functools.reduce(lambda x, y: x + y, sorted(uname))
        if uname == res:
            result.append('NO')
        else:
            result.append('YES')
    return result


n = int(input())
usernames = []
for _ in range(n):
    temp = input()
    usernames.append(temp)

result = possibleChanges(usernames)
for i in result:
    print(i)
