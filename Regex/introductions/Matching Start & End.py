""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 19-12-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Matching Start & End
#problem link: https://www.hackerrank.com/challenges/matching-start-end/problem?isFullScreen=false

Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
