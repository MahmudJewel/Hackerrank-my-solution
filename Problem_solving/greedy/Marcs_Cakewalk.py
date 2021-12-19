""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 09-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Marc's Cakewalk
# problem link: https://www.hackerrank.com/challenges/marcs-cakewalk/problem

n=int(input())
arr=list(map(int,input().strip().split()))
arr.sort(reverse=True)
res=0
for i in range(n):
	res+=2**i*arr[i]
print(res)