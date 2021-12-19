""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 07-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Append and Delete
#problem link: https://www.hackerrank.com/challenges/append-and-delete/problem

'''''''''
There are three case.
case 1: length(initial string)>length(desire string)
such as==> abcd, abf
for every case there are 3 condition for 'Yes'
i) delete+append==given operation  ==>abcd,abf,3
ii) (given operation-(delete+append))%2==0 ==>abcd, abf, 5
iii) (given operation-(delete+append))>0 ==>abcd, a, 2
common case: iv) length(initial string)+length(desire string)<=given operation ==>abcd, abf, 7 or more. As you can delete as you want

case 2: length(initial string)<length(desire string)
such as==> abf, abcd
i) delete+append==given operation  ==>abf, abcd, 3
ii) (given operation-(delete+append))%2==0 ==>abf, abcd, 5
iii) (given operation-(delete+append))>0 ==>a, abcd, 2
common case: iv) length(initial string)+length(desire string)<=given operation ==>abf, abcd, 7 or more. As you can delete as you want

case 3: length(initial string)==length(desire string)
such as==> abf, abf
i) delete+append==given operation  ==>abf, abc, 2
ii) (given operation-(delete+append))%2==0 ==>abf, abc, 4
common case: iii) length(initial string)+length(desire string)<=given operation ==>abf, abf, 7 or more. As you can delete as you want


'''

def sresult(str,mstr,n,l1,l2):
    t=0
    for temp in range(l2):  #For finding matching position
        if(str[temp]==mstr[temp]):
            t+=1
        else: break
    ans=l1-t+l2-t     #Delete(l1-t)+append(l2-t) operation
    if(ans==n or ((n-ans)%2==0 and (n-ans)>0)):   #n-ans>0 ==>abcde,a,2
        return 'Yes'  #if operation match or operation is more than couple times than given operartion.
    else:
        return 'No'

def mresult(str,mstr,n,l1,l2):
    t=0
    for temp in range(l1):
        if(str[temp]==mstr[temp]):
            t+=1
        else: break
    ans=l1-t+l2-t
    if(ans==n or (n-ans)%2==0 and n<l2 ): return 'Yes'
    else: return 'No'

str,mstr,n=input().strip(),input().strip(),int(input())
l1,l2=len(str),len(mstr)
#common case
if(l1+l2<=n):
    print('Yes')
#case 1
elif(l1>l2):
    print(sresult(str,mstr,n,l1,l2))
#case 2
elif(l2>l1):
    print(mresult(str, mstr, n, l1, l2))
#case 3
elif(l1==l2):
    print(sresult(str,mstr,n,l1,l2))

