#v) Write a function
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 26-10-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Write a function

# divisible 400 ==> leap year.
# divisible 4 but not 100 ==> leap year.

def is_leap(year):
    if(year%100==0):
        if(year%400==0):
            return True
        return False
    elif(year%4==0):
        return True
    return False

year = int(input())
print(is_leap(year))