import math

class Perceptron(object):
    def __init__(self):
        self.weights = [0.5, 0.5]

    def activationFunction(self, weightedSum):
        # sigmoid function
        return 1 / (1 + math.exp(-weightedSum))
    
    def activationFunction2(self, weightedSum):
        #stepActivatio function
        if weightedSum < 0:
            return 0
        elif weightedSum >= 0:
            return 1

    def output(self, inputs):
        weightedSum = 0
        for i in range(len(inputs)):
            weightedSum += inputs[i] * self.weights[i]
        return self.activationFunction(weightedSum)

neuron = Perceptron()
print(neuron.output([0, -5]))
neuron2 = Perceptron()
print(neuron2.output([-3, -2]))
neuron_Output=neuron.output([0, -5])
neuron2_Output=neuron2.output([-3,-2])
neuron3 = Perceptron()
print(neuron3.output([neuron_Output , neuron2_Output]))