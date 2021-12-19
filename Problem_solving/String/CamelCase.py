""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 15-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: CamelCase
# problem link: https://www.hackerrank.com/challenges/camelcase/problem

'''
#Solve 1
s=input()
s=''.join(sorted(s))
#print(s)
ans=1
#print(ans)
for i in s:
	if(i.islower() ):
		break
	ans+=1
print(ans)
'''


#sove2 
s=sum(map(str.isupper,input().strip()))+1
print(s)



