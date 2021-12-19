""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 31-10-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Caesar Cipher
# problem link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=false

uppercase=[chr(x) for x in range(65, 91)]
lowercase=[chr(x) for x in range(97, 123)]
def Caesar_Cipher(letter, k):
    result=''
    for x in letter:
        temp=ord(x)+k
        if (x in uppercase): # if uppercase
            temp2 = temp%91
            temp=temp2+65
            result+=chr(temp)
        elif(x in lowercase): # if lowercase
            if(temp>122):
                temp=temp-122+96
            result+=chr(temp)
        else:                 # if other character
            result+=x
            
    return result

length = int(input())
letter = input()
k=int(input())
result=Caesar_Cipher(letter, k)
print(result)
