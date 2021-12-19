""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 08-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Sock Merchant
# problem link: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

n=int(input())
arr=list(map(int,input().strip().split()))
arr.sort()
i,res=1,0
while(i<n):
	if(arr[i]==arr[i-1]):
		res+=1
		i+=2
	else:
		i+=1
print(res)

