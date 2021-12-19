""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 27-04-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Find the Runner-Up Score!
#problem link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def runner(array,n):
    array.sort()
    for i in range(n-1,-1,-1):
        if(i==0):
            return array[i]
        if(array[i]!=array[i-1]):
            return array[i-1]

    return 0

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    result = runner(arr,n)
    print( result )