""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 05-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: sWAP cASE
#problem link: https://www.hackerrank.com/challenges/swap-case/problem


'''''''''
#solve 1
def swap_case(s):
    temp=ord('a')-ord('A')  #char to ascii
    ss=''
    for i in s:
        dec=ord(i)
        if(dec>64 and dec<91): #Uppercase
            ss+=chr(temp+dec)
        elif(dec>96 and dec<123): #lowercase
            ss += chr(dec-temp)
        else:
            ss+=i
    return ss

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''''


'''''''''
#solve 2. not compatible but works
print(input().swapcase())
'''


#solve 3
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)