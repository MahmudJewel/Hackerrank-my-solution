""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 15-08-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Company Logo
# problem link: https://www.hackerrank.com/challenges/most-commons/problem

#'''
s=input()
dc={}
#s=sorted(s,reverse=True)
#print(s)

for i in s:
	dc[i]=s.count(i)
dc2={}
dc2=sorted(dc.items(), key=lambda x:x[1])

temp=0
for i in dc2:
	print(i,dc2[i])
	temp+=1
	if(temp>=3):
		break



'''
dic={2:90, 1: 100, 8: 3, 5: 67, 3: 5}
dic2={}
print(dic.values())
for i in sorted(dic):
   dic2[i]=dic[i]
print(dic2)
'''