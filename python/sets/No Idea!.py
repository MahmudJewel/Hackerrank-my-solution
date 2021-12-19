""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 01-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name:
#problem link:

"""
#OK
m=list(map(int,input().split()))
mine=list(map(int,input().split()))
happy=set(map(int,input().split()))
sad=set(map(int,input().split()))
sum=0
for i in range(m[0]):
    if(mine[i] in happy):
        sum+=1
    if (mine[i] in sad):
        sum -= 1
print(sum)
"""
m,n=map(int,input().split())
mine=list(map(int,input().split()))
happy=set(map(int,input().split()))
sad=set(map(int,input().split()))
sum=0
for i in mine:
    sum+=((i in happy)-(i in sad))
print(sum)
