class Perceptron(object):
    weights = [150, 200, 175]
    def activationFunction(self, weightedSum):
    # funzione gradino
        if weightedSum > 0:
            ret = 1.0
        else:
            ret = 0
        return ret

    def output(self, inputs):
        weightedSum = self.weights[0]
        for i in range(len(inputs)):
            weightedSum += inputs[i] * self.weights[i + 1]
        return self.activationFunction(weightedSum)
    def learn(self, x, yAtteso):
        yCalcolato = self.output(x)
        error = yAtteso - yCalcolato
        print("input", x, "yAtteso", yAtteso, "error", error)
        learningRate = 0.01
# aggiorno peso del bias

        self.weights[0] += learningRate * error
# aggiorno i pesi degli input del perceptron
        for i in range(len(self.weights) - 1):
            self.weights[i + 1] += learningRate * error * x[i]

neuron = Perceptron()
# Dati per addestramento
# tabella della verità della AND
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 0, 0, 1]
# Addestramento
for epoch in range(100):
    print("epoch:", epoch)
    for i, x in enumerate(X):
        yAtteso = Y[i]
        neuron.learn(x, yAtteso)
# verifica dell'addestramento
print(neuron.output([0, 0]))
print(neuron.output([0, 1]))
print(neuron.output([1, 0]))
print(neuron.output([1, 1]))
print("Weight: ", neuron.weights)