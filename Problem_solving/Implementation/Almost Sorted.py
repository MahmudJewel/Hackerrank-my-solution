""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 08-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Almost Sorted
# problem link: https://www.hackerrank.com/challenges/almost-sorted/problem

size,array=int(input()),list(map(int,input().strip().split()))
temp=0
for i in range(len(array)-1):
    if(array[i]>array[i+1]):
        array[i],array[i+1]=array[i+1],array[i]
        if(array==sorted(array)):
            print("Yes\nSwap",i,i+1)
        else:
            array[i],array[i+1]=array[i+1],array[i]
            for j in range(i+1,len(array)-1):
                if (array[j] > array[j + 1]):
                    array[j+1], array[i] = array[i], array[j+1]
                    if (array == sorted(array)):
                        print("Yes\nSwap", i+1, j+2)
                    else:
                        array[j+1], array[i] = array[i], array[j+1]
                    break
        break