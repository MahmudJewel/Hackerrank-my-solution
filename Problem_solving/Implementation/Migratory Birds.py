""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 07-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Migratory Birds
#problem link: https://www.hackerrank.com/challenges/migratory-birds/problem

n,li=int(input()), list(map(int,input().split()))
num,occur=0,0
for i in range(1,6):
    temp=li.count(i)
    if(temp>occur):
        occur,num=temp,i
print(num)