""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 01-03-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Alphabet Rangoli
#problem link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem


'''
main_string="0abcdefghijklmnopqrstuvwxyz"
ls=[]
n=int(input())
temp=1
for i in range(0,n,1):
	substring=main_string[n:n-1-i:-1]+main_string[n-i+1:n+1:1]
	ls_string='-'*(2*(n-1-i))+'-'.join(substring)+'-'*(2*(n-1-i))
	ls.append(ls_string)
for i in range(n-2,-1,-1):
	ls.append(ls[i])
for i in range(2*n-1):
	print(ls[i])
'''

def print_rangoli(n):
	main_string="0abcdefghijklmnopqrstuvwxyz"
	ls=[]
	for i in range(0,n,1):
		substring=main_string[n:n-1-i:-1]+main_string[n-i+1:n+1:1]
		ls_string='-'*(2*(n-1-i))+'-'.join(substring)+'-'*(2*(n-1-i))
		ls.append(ls_string)
	for i in range(n-2,-1,-1):
		ls.append(ls[i])
	for i in range(2*n-1):
		print(ls[i])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)