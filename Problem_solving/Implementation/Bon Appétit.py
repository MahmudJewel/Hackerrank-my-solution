""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 08-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Bon Appétit
#problem link: https://www.hackerrank.com/challenges/bon-appetit/problem

n,nota=map(int,input().split())
li=list(map(int,input().strip().split()))
apaid=int(input())
li.remove(li[nota])
sum=sum([i for i in li])
sum=int(sum/2)
if(apaid==sum):
    print('Bon Appetit')
else:
    print(apaid-sum)
