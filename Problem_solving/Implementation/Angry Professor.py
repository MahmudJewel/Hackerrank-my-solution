""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 22-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Prepare>Algorithms>Implementation>Angry Professor
# problem link: https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=false

t=int(input())
for _ in range(t):
    num_of_student, cancellation_thresold=map(int, input().split())
    arrival_time=list(map(int, input().strip().split()))
    in_time=0
    for i in arrival_time:
        if i<=0:
            in_time=in_time+1
    if in_time>=cancellation_thresold:
        print('NO')
    else:
        print('YES')

