""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 18-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Capitalize!
#problem link: https://www.hackerrank.com/challenges/capitalize/problem


#!/bin/python3

import math
import os
import random
import re
import sys

'''
#solve 1
# Complete the solve function below.
def solve(s):
	s=s.strip()
	ss=s[0].upper()
	for i in range(1,len(s)):
		if(s[i-1]==' '):
			ss+=s[i].upper() 
		else: 
			ss=ss+s[i] 
	return ss
'''

#solve 2
def solve(s):
	return (' '.join(i.capitalize() for i in s.split(' ')))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
