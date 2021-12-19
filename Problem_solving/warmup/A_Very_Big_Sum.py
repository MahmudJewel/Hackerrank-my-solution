""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 16-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: A Very Big Sum
#problem link: https://www.hackerrank.com/challenges/a-very-big-sum/problem


'''
#solve 1
def reverse(s):
	str=''
	for i in s:
		str=i+str
	return str


def add(a1,a2):
	l1,l2=len(a1),len(a2)
	a1,a2=reverse(a1),reverse(a2)
	#print(a1,a2)
	if(l2>l1):
		a1,a2,l1,l2=a2,a1,l2,l1
	ans,result,rem,i,temp='',0,0,0,0
	for i in range(l2):
		sum=int(a1[i])+int(a2[i])+temp
		rem,result=sum%10,int(sum/10)
		ans+=str(rem)
		temp=result
	
	for j in range(i+1,l1):
		sum=int(a1[j])+temp
		rem,result=sum%10,int(sum/10)
		ans+=str(rem)
		temp=result

	if(temp>0):
		ans+=str(temp)
	ans=reverse(ans)
	return ans

n,s=int(input()),input().strip().split()

a1,a2=s[0],s[1]
ab=add(a1,a2)
for i in range(2,len(s)):
	ab=add(ab,str(s[i]))
print(ab)
'''

n,s=int(input()),input().strip().split()
print(sum(int(i) for i in s))
