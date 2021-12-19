""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 27-10-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: The Hurdle Race
# problem link: https://www.hackerrank.com/challenges/the-hurdle-race/problem

# Solution==>1
# n=list(map(int, input().strip().split()))
# height = list(map(int, input().strip().split()))
# max_value=max(height)
# result=max_value-n[1]
# if (result<=0):
#     print(0)
# else:
#     print(result)



# Solution ==> 2
def The_Hurdle_Race(k, height):
    print(max(max(height)-k,0))

n,k = map(int, input().strip().split())
# print(f"type {type(n)}")
height=list(map(int, input().strip().split()))
The_Hurdle_Race(k, height)