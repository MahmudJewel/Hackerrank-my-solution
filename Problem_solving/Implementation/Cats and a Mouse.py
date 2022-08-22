""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 22-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Prepare>Algorithms>Implementation>Cats and a Mouse
# problem link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=false

q=int(input())
for i in range(q):
    x,y,z=map(int, input().split())
    catA=abs(x-z)
    catB=abs(y-z)
    if catA==catB:
        print('Mouse C')
    elif catA<catB:
        print('Cat A')
    elif catB<catA:
        print('Cat B')
