""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 07-03-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

main_data=list(map(int, input().strip().split()))
print(main_data)

l=len(main_data)
for i in range(l):
	for j in range(l-1):
		if(main_data[j]>main_data[j+1]):
			main_data[j],main_data[j+1]=main_data[j+1],main_data[j]  #swap


print(main_data)