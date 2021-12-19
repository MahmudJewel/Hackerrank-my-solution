""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 05-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Find a string
#problem link: https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen



'''''''''
#solve 1
def count_substring(string, sub_string):
    ans=0
    l=len(string)-len(sub_string)+1
    for i in range(l):
        if(string[i:i+len(sub_string)]==sub_string):
            ans+=1
    return ans

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

'''''

#solve 2
str=input().strip()
sub_str=input().strip()
print(sum ( [1 for i in range(len(str)-len(sub_str)+1) if(str[i:i+len(sub_str)]==sub_str)]))
