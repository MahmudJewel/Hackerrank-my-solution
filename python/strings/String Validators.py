""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 06-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: String Validators
#problem link: https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen


'''''''''
#solve 1
str=input()
aln,alp,dig,low,upper=False,False,False,False,False
for i in str:
    if(i.isalnum()): aln=True
    if(i.isalpha()): alp=True
    if(i.isdigit()): dig=True
    if (i.islower()): low = True
    if (i.isupper()): upper = True
print(aln)
print(alp)
print(dig)
print(low)
print(upper)
'''''


'''''''''
#solve 2
str=input()
result=[False for i in range(5)]
for i in str:
    if(i.isalnum()): result[0]=True
    if(i.isalpha()): result[1]=True
    if(i.isdigit()): result[2]=True
    if (i.islower()):result[3]=True
    if (i.isupper()):result[4]=True
for i in result:
    print(i)
'''''


#solve 3
str=input()
li=['isalnum()','isalpha()','isdigit()','islower()','isupper()']
for test in li:
    print(any(eval('c.' + test) for c in str))



