""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 05-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Picking Numbers
# problem link: https://www.hackerrank.com/challenges/picking-numbers/problem


l=int(input())
arr=list(map(int,input().strip().split()))
arr.sort()
maxlen=0
for i in range(l):
	temp=1
	for j in range(i+1,l,1):
		if(abs(arr[i]-arr[j])>1):
			break
		else:
			temp+=1
	if(temp>maxlen):
		maxlen=temp
print(maxlen)
