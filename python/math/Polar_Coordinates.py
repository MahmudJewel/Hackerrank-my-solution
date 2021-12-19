""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 02-06-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Polar Coordinates
#problem link: https://www.hackerrank.com/challenges/polar-coordinates/problem


'''
import cmath, math

x=complex(input())
xr=math.sqrt(x.real**2+x.imag**2)
xp=cmath.phase(x)
print('{:.3f}\n{:.3f}'.format(xr,xp))
'''


import cmath
print(*cmath.polar(complex(input())), sep='\n')



