""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 00-04-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Map and lambda Function
#problem link:

cube = lambda x:x**3

def fibonacci(n):
    if (n==0):
        return []
    elif(n==1):
        return [0]

    a, b = 0, 1
    arr = list(range(n))
    arr[0], arr[1] = a, b
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        arr[i]=c
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
