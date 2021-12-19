""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 05-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: String Split and Join
#problem link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?h_r=next-challenge&h_v=zen

'''''''''
#solve 1
def split_and_join(line):
    str=''
    for i in line:
        if (i==' '):
            str+='-'
        else:
            str+=i
    return str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
'''''

#solve 2
#print(input().replace(' ','-'))

#solve 3
print("-".join(input().split()))
