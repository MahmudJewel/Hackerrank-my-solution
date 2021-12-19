""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 14-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Drawing Book 
# problem link: https://www.hackerrank.com/challenges/drawing-book/problem

n,p=int(input()),int(input())
fres,bres=0,0
i=1
if(n%2==1):
	j=n-1
else:
	j=n
while(1):
	if(i>=p or j<=p):
		break
	bres+=1
	fres+=1
	i+=2
	j-=2
print(min(fres,bres))
