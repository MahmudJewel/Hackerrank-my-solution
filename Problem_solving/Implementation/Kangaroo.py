""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 05-07-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Kangaroo
# problem link: https://www.hackerrank.com/challenges/kangaroo/problem


x1,v1,x2,v2=[int(x) for x in input().split()]
if(v2>=v1):
	print('NO')

else:
	i=1
	while(1):
		d1=x1+v1*i
		d2=x2+v2*i
		if(d1==d2):
			print('YES')
			break
		elif(d1>d2):
			print('NO')
			break
		i+=1
