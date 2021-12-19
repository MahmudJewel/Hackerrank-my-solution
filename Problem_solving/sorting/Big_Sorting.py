""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 16-06-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Big Sorting
#problem link: https://www.hackerrank.com/challenges/big-sorting/problem


ar=[input() for _ in range(int(input()))]
result=sorted(ar, key = lambda x: (len(x),x))
for i in result:
	print(i)

