""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 04-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Lists
#problem link: https://www.hackerrank.com/challenges/python-lists/problem


'''''''''
#solve 1
#ok
my_List=[]
for i in range(int(input())):
    temp=input().split()
    temp2 = list(map(int, temp[1:]))
    if(temp[0]=='insert'):
        my_List.insert(temp2[0],temp2[1])
    elif(temp[0]=='append'):
        my_List.append(temp2[0])
    elif(temp[0]=='remove'):
        my_List.remove(temp2[0])
    elif(temp[0]=='sort'):
        my_List.sort()
    elif(temp[0]=='reverse'):
        my_List.reverse()
    elif(temp[0]=='pop'):
        my_List.pop()
    else:
        print(my_List)
'''

#solve 2
n = int(input())
l = []
for _ in range(n):
    s =input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)

    else:
        print (l)


