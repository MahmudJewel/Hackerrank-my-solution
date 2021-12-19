

n=int(input("Enter the number of data: "))
print("Enter the input data set: ")
pre_syn_sig=[float(input()) for _ in range(n)]
total=0.0
for i in range(n):
	total+=pre_syn_sig[i]
xmean=total/n

print("Enter the weights: ")
weights=[float(input()) for _ in range(n)]
l_rate=float(input("Enter the learning rate: \n"))
bias=float(input("Enter the bias: \n"))
ysum=0.0
for it in range(int(input("Enter the iteration: "))):
	sum=0.0
	for i in range(n):
		sum+=pre_syn_sig[i]*weights[i]
	post_syn_sig=sum+bias
	ysum+=post_syn_sig
	ymean=ysum/(it+1)
	print("Weights : ", weights,"output: ", post_syn_sig)
	

	for i in range(n):    #Hebbian learning
		dell=l_rate*(pre_syn_sig[i]-xmean)*(post_syn_sig-ymean)
		weights[i]+=dell