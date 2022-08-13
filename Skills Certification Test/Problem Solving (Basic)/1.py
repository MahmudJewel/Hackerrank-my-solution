


def minTime(files, numCores, limit):
    # Write your code here
	files.sort(reverse=True)
	# print(files)
	for i in range(len(files)):
		if limit==0:
			break
		if files[i]%numCores==0:
			files[i]=int(files[i]/numCores)
			limit=limit-1
	sum=0
	for i in files:
		sum=sum+i 
	return sum 


n=int(input())
files=[]
for _ in range(n):
	files.append(int(input()))
numCores=int(input())
limit=int(input())

result=minTime(files, numCores, limit)
print(result)