""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 08-03-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

'''
n=list(map(int,input().strip().split()))
l=len(n)
for i in range(l-1):
	temp=n[i+1]
	for j in range(i+2,l,1):
		temp2=n[j]
		if(temp>temp2):
			temp=temp2
	if(temp<n[i]):
		ls=n[i:]   # for avoiding duplicate value condition
		it=ls.index(temp)
		n[i],n[it+i]=n[it+i],n[i]  #swap
print(n)
'''

n=list(map(int,input().strip().split()))
l=len(n)
for i in range(l-1):
	mini=i+1
	for j in range(i+2,l,1):
		if(n[mini]>n[j]):
			mini=j
	if(n[i]>n[mini]):
		n[i],n[mini]=n[mini],n[i]
print(n)