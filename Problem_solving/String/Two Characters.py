""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 27-10-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Two Characters
# problem link: https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=false

# ******* will solve this *************

def Two_Characters(sen):
    st=set(sen)
    lst=list(st)
    cnt=[]
    for i in lst:
        cnt.append(sen.count(i))
    cnt.sort(reverse=True)
    #result = cnt
    for i in cnt:
        if i in cnt[cnt.index(i)+1:]:
            result=2*i
            return result
        elif i-1 in cnt:
            result=2*i-1
            return result
    return result

length=int(input())
sentence=input()
result=Two_Characters(sentence)
print(result)

# a=[1,2,3,4,5,8]
# print(a.index(9))
