""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 03-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Missing Numbers
#problem link: https://www.hackerrank.com/challenges/missing-numbers/problem

a1,arr1=int(input()), list(map(int,input().strip().split()))
a2,arr2=int(input()), list(map(int,input().strip().split()))
result=[]
for x in sorted(set(arr2)):
	if arr1.count(x)!=arr2.count(x):
		result.append(x)
print(*(result))