""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 22-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Prepare>Algorithms>Implementation>Beautiful Days at the Movies
# problem link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=false

def revercify(num):
    st=''
    while num:
        rem=num%10
        num=int(num/10)
        st=st+str(rem)
    result=int(st)
    return result

start, end, divisor=map(int, input().strip().split())
beautiful_days=0
for i in range(start, end+1):
    temp=revercify(i)
    result=abs(i-temp)
    if result%divisor==0:
        beautiful_days=beautiful_days+1
print(beautiful_days)

