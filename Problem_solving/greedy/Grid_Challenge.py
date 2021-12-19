""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 10-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Grid Challenge
# problem link: https://www.hackerrank.com/challenges/grid-challenge/problem

def grid(arr,n):
	for i in range(n):
		arr[i]=sorted(arr[i])
	for i in range(len(arr[0])):
		for j in range(1,len(arr[0])):
			if(arr[j-1][i]>arr[j][i]):
				return 'NO'
	return 'YES'


for i in range(int(input())):
	l=int(input())
	arr=[]
	for j in range(l):
		arr.append(input().strip())
	print(grid(arr,l))
