""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 19-12-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Matching Word & Non-Word Character
#problem link: https://www.hackerrank.com/challenges/matching-word-non-word/problem?isFullScreen=false

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
