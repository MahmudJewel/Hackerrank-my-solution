""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 06-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Merge the Tools!
#problem link: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    l=len(string)
    for i in range(0,l+1,k):
        str=string[i:k+i]
        se=set(str)
        #print(se)
        ss=''
        for j in se:
            ss+=j
        print(ss)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)