""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 17-12-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Matching Digits & Non-Digit Characters
#problem link: https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem?isFullScreen=false

Regex_Pattern = r"\d{2}\D{1}\d{2}\D{1}\d{4}"	# Do not delete 'r'.


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
