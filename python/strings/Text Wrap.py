""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 07-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Text Wrap
#problem link: https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    temp,str,l=1,'',len(string)
    for i in range(0,l,max_width):
        s=string[i:max_width*temp]
        temp+=1
        str=str+s+'\n'
    return str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)