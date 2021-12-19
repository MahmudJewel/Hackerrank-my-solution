""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 02-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Nested Lists
#problem link: https: https://www.hackerrank.com/challenges/nested-list/problem

'''''''''
#solve 1
#it's ok
if __name__ == '__main__':
    array=[]
    for _ in range(int(input())):  #input
        name = input()
        score = float(input())
        array.append([name,score])

    array.sort(key=lambda x:x[1])  #short array according to second row
    l=len(array)
    temp=0
    for temp in range(l-1):        #smallest value index
        if(array[temp][1]!=array[temp+1][1]):
            break

    final=[]
    final.append(array[temp+1][0]) #one second smallest value
    for i in range(temp+2,l):      # all second smallest value
        if(array[i][1]==array[i-1][1]):
            final.append(array[i][0])
        else:
            break
    final.sort()
    for i in range(len(final)):
        print(final[i])
'''

#solve 2
if __name__ == '__main__':
        marksheet=[[input(),float(input())] for _ in range(int(input()))]
        second=sorted(list(set([b for a,b in marksheet])))[1]
        print('\n'.join([a for a, b in sorted(marksheet) if b == second]))


