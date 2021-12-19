""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 05-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Sherlock and Array
# problem link: https://www.hackerrank.com/challenges/sherlock-and-array/problem

'''
#runtime error.
n=int(input())
for p in range(n):
	l=int(input())
	arr=list(map(int,input().split()))
	temp,temp2=1,0
	if(sum(arr[1:])==0):
		print('YES')
	else:
		while(temp<l):
			if(sum(arr[:temp])==sum(arr[temp+1:])):
				print('YES')
				temp2=1
				break
			else:
				temp+=1
		if(temp2==0):
			print('NO')
'''


'''
#Runtime error
def result(arr,l):
	if(l==1):
		return 'YES'
	for i in range(l-1):
		if(sum(arr[:i])==sum(arr[i+1:])):
			return 'YES'
	return 'NO'

n=int(input())
for p in range(n):
	l=int(input())
	arr=list(map(int,input().split()))
	print(result(arr,l))
'''



def result(arr,l):
	if(l==1):
		return 'YES'
	left=0
	right=sum(arr)-arr[0]
	for i in range(l-1):
		if(left==right):
			return 'YES'
		else:
			right=right-arr[i+1]
			left=left+arr[i]
	return 'NO'

n=int(input())
for p in range(n):
	l=int(input())
	arr=list(map(int,input().split()))
	print(result(arr,l))

