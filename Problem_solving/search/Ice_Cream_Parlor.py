""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 18-06-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Ice Cream Parlor
#problem link: https://www.hackerrank.com/challenges/icecream-parlor/problem

test=int(input())
for i in range(test):
	n,m,arr=int(input()),int(input()), list(map(int,input().strip().split()))
	for i in range(m):
		for j in range(i+1,m):
			if (arr[i]+arr[j]==n):
				print(i+1, j+1)
				break

