""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 27-10-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Counting Valleys
# problem link: https://www.hackerrank.com/challenges/the-hurdle-race/problem

# Sol==>1
def Counting_Valleys(path):
    result,counting=0,0
    for i in path:
        temp=0
        if(i=='U'):
            temp=1
        else:
            temp=-1
        counting+=temp
        if(counting==0 and i=='U'):
            result+=1
    print(result)

# Sol ==> 2
def Counting_Valleys2(path):
    result, counting=0,0
    for i in path:
        counting += 1 if i=='U' else -1
        if(counting==0 and i =='U'):
            result+=1
    print(result)




length=int(input())
path=input()
Counting_Valleys2(path)