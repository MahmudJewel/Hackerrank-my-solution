""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 08-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Minimum Loss
# problem link: https://www.hackerrank.com/challenges/minimum-loss/problem

n=int(input())
arr=list(map(int,input().strip().split()))
arr2=sorted(arr,reverse=True)
print(arr2)
mn=10**16
for i in range(1,n):
	d=arr2[i-1]-arr2[i]
	if((d<mn) and (arr.index(arr2[i])>arr.index(arr2[i-1]))):
		mn=d
print(mn)


