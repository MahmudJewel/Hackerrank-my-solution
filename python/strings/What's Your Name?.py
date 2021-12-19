""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 05-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: What's Your Name?
#problem link: https://www.hackerrank.com/challenges/whats-your-name/problem

'''''''''
#solve 1
def print_full_name(a, b):
    print("Hello",a,b+'!',"You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
'''

#solve 2
print("Hello",input(),input()+'!',"You just delved into python.")