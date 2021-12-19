""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 08-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Pairs
# problem link: https://www.hackerrank.com/challenges/pairs/problem

'''
#solve 1
n,k=[int(x) for x in input().strip().split()]
arr=list(map(int,input().strip().split()))
arr.sort(reverse=True)
res=0
for i in range(n):
	for j in range(i+1,n):
		if(arr[i]-arr[j]>k):
			break
		elif(arr[i]-arr[j]==k):
			res+=1
print(res)
'''

#solve 2 with O(N)
n,k=[int(x) for x in input().strip().split()]
arr=list(map(int,input().strip().split()))
arr.sort(reverse=True)
i,j,res=0,1,0

while(j<n):
	d=arr[i]-arr[j]
	if(d==k):
		res+=1
		j+=1
	elif(d>k):
		i+=1
	elif(d<k):
		j+=1
print(res)

