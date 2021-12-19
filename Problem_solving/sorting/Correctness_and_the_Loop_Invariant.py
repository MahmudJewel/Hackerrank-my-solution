""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 16-06-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Correctness and the Loop Invariant
#problem link: https://www.hackerrank.com/challenges/correctness-invariant/problem

n,arr=int(input()), list(map(int,input().strip().split()))
ss=''
for i in sorted(arr):
	ss+=str(i)+' '
print(ss.strip())