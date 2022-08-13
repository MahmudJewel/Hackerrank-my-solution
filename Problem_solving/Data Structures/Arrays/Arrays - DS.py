""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 11-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: PrepareData > Structures > Arrays > Arrays - DS
#problem link: https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=false

n=int(input())
lst=list(map(int, input().strip().split()))
# print(lst)
temp=[]
for i in range(n):
    temp.append(lst[n-1-i])
print(*temp)
