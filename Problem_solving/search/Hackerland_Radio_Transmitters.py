""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 07-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Hackerland Radio Transmitters
# problem link: https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem


'''
#solve 1
n,k=[int(x) for x in input().split()]
arr=list(map(int,input().split()))
st=set(arr)
arr=list(st)
arr.sort()
n=len(arr)
c,i=0,0
while(i<n):
	c+=1
	mid=arr[i]+k
	j=i
	while(i<n and mid>=arr[i]):
		i+=1
	if(j==i+1):
		continue
	right=arr[i-1]+k
	while(i<n and right>=arr[i]):
		i+=1
print(c)
'''

#solve 2
n,k=[int(x) for x in input().split()]
arr=list(map(int,input().split()))
st=set(arr)
arr=list(st)
arr.sort()
n=len(arr)
temp1=0
result=0
while(temp1<n):
	result+=1
	temp2=temp1
	while(temp2<n and arr[temp2]-arr[temp1]<=k):
		temp2+=1

	temp3=temp2-1
	temp1=temp3
	while(temp3<n and arr[temp3]-arr[temp1]<=k):
		temp3+=1
	temp1=temp3
print(result)
