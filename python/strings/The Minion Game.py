""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 07-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: The Minion Game
#problem link: https://www.hackerrank.com/challenges/the-minion-game/problem

'''''''''
#time limit
def minion_game(str):
    strt,kvn=0,0
    vowel=['A','E','I','O','U']
    l = len(str)
    temp = 0
    for i in range(l):
        a, b = 0, 1 + i
        for j in range(l - i):
            #s=str[a:b]
            if (str[a] in vowel):
                kvn+=1
            else:
                strt+=1
            a, b = a + 1, b + 1
    if(kvn>strt):
        print("Kevin",kvn)
    elif(kvn==strt):
        print("Draw")
    else:
        print("Stuart",strt)


if __name__ == '__main__':
    s = input()
    minion_game(s)

'''''

'''''''''
#solve 2 ok
def minion_game(str):
    l=len(str)
    vw='AEIOU'
    kvn,strt=0,0
    for i in range(l):
        if(str[i] in vw):
            kvn=kvn+l-i
        else:
            strt=strt+l-i
    if(kvn>strt):
        print("Kevin",kvn)
    elif(strt>kvn):
        print('Stuart',strt)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
'''''


#solve 3
def minion_game(str):
    l,vw=len(str),'AEIOU'
    kvn=sum([l-i for i in range(l) if str[i] in vw])
    strt=int(l*(l+1)/2-kvn)
    if (kvn > strt):
        print("Kevin", kvn)
    elif (strt > kvn):
        print('Stuart', strt)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
