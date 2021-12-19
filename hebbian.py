'''
import numpy as np

class NeuralNetwork:
    
    def __init__(self):
        np.random.seed(1)
        
        self.synaptic_weights = np.random.random((3, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        
        for i in range(training_iterations):
            output = self.think(training_inputs)

            error = training_outputs - output
            
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":

    neural_network = NeuralNetwork()

    print("Beginning Randomly Generated Weights: ")
    print(neural_network.synaptic_weights)

    #training data consisting of 4 examples--3 input values and 1 output
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    neural_network.train(training_inputs, training_outputs, 15000)

    #print("Ending Weights After Training: ")
    #print(neural_network.synaptic_weights)

    x0 = int(input("User Input One: "))
    x1 = int(input("User Input Two: "))
    x2 = int(input("User Input Three: "))
    
    print("Considering New Situation: ", x0,x1,x2)
    print("New Output data: ")
    y=neural_network.think(np.array([x0,x1,x2]))
    print(y)
    w0,w1,b=0.0,0.0,0.0
    for it in range(100):
    	w0+=.02*x0*y
    	w1+=.02*x1*y
    	b+=y
    print(w0,w1,b)
    '''

n=int(input("Enter the number of data: "))
print("Enter the input data set: ")
pre_syn_sig=[float(input()) for i in range(n)]
print("Enter the weights: ")
weights=[float(input()) for _ in range(n)]
l_rate=float(input("Enter the learning rate: \n"))
bias=float(input("Enter the bias: \n"))
for it in range(int(input("Enter the iteration: "))):
	sum=0
	for i in range(n):
		sum+=pre_syn_sig[i]*weights[i]
	post_syn_sig=sum+bias
	print("Weights : ", weights,"output: ", post_syn_sig)
	

	for i in range(n):    #Habbian learning
		weights[i]+=(l_rate*pre_syn_sig[i]*post_syn_sig)
