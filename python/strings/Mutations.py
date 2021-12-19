""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 05-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Mutations
#problem link: https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen


'''''''''
#solve 1
def mutate_string(string, position, character):
    str=''
    l=len(string)
    for i in range(l):
        if(i==position):
            str+=character
        else:
            str+=string[i]

    return str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
'''''


#solve 2
def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
