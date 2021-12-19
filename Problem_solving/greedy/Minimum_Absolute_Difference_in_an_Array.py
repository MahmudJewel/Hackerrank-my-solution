""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 09-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Minimum Absolute Difference in an Array
# problem link: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

n=int(input())
arr=list(map(int,input().strip().split()))
arr.sort()
res=2*10**9
for i in range(1,n):
	if(abs(arr[i]-arr[i-1])<res):
		res=abs(arr[i]-arr[i-1])
print(res)
