""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 16-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Strong Password
# problem link: https://www.hackerrank.com/challenges/strong-password/problem


le,str=int(input()),input().strip()
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

n,l,u,s=1,1,1,1

for i in str:
	if(i in numbers): n=0
	if(i in lower_case): l=0
	if(i in upper_case): u=0
	if(i in special_characters): s=0
missing=n+l+u+s
print(missing) if((missing+le>5)) else print(6-le)
