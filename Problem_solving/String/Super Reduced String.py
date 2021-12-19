""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 12-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Super Reduced String
# problem link: https://www.hackerrank.com/challenges/reduced-string/problem

str=input()
i=1
while(i<len(str)):
    if(str[i]==str[i-1]):
        str=str[:i-1]+str[i+1:]
        i=1
    else:i+=1
print("Empty String") if len(str)==0 else print(str)
