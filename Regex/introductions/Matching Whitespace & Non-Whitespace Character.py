""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 19-12-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Matching Whitespace & Non-Whitespace Character
#problem link: https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem?isFullScreen=false

Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
