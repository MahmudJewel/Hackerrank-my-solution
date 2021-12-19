""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 28-10-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Alphabet Rangoli
#problem link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def Electronics_Shop(balance, keyboard, drivers):
    result=-1
    keyboard=sorted(keyboard, reverse=True)
    drivers=sorted(drivers, reverse=True)
    for i in keyboard:
        for j in drivers:
            temp=i+j
            if(temp<=balance and temp>result):
                result=temp
    return result

b, n, m = map(int, input().strip().split())
keyboard=set(map(int, input().strip().split()))
drivers=set(map(int, input().strip().split()))
result = Electronics_Shop(b, keyboard, drivers)
print(result)



