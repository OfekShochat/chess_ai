from yannl.yannlerrors import *
import yannl.activations
from time import time

class layers:
    """
    layerparhms be like: {"neuron0":{"weights":{"w1":w1, "w2":w2...}, "bias":bias}, "neuron1":"weights":{"w1":w1, "w2":w2...}, "bias":bias}} you can change "bias" to just "b" and "weights" to "ws". or we can do neurons with a class.
    """
    def __init__(self, layerparhms: dict):
        self.layerparhms = layerparhms
        self.weights = self.findws()
        self.bias = self.findbias()
    def findbias(self):
        for i in self.layerparhms:
            for n in i:
                if n == "b": return self.layerparhms[i]
                if n == "bias": return self.layerparhms[i]
        raise NoBiasErr("no bias given in " + str(self.layerparhms))
    def findws(self):
        for i in self.layerparhms:
            if i == "ws": return self.layerparhms["ws"]
            if i == "weights": return self.layerparhms["weights"]
        raise noWeightsErr("no weights were given in " + str(self.layerparhms))

    def make_weights_from_neurons(self, num_of_neurons):
        self.weights = {}
        self.bias = 0
        for i in range():
            self.weights.update({"w" + i: "w" + i})

class inputLayer(layers):
    def __init__(self, layerparhms, num_of_neurons, activation_function):
        super().__init__(layerparhms)
        self.purpose = "input"
        self.num_of_neurons = num_of_neurons
        self.activation_function = activation_function
        if self.activation_function.strip() == "knock knock":
            if input("knock knock: ") == "who is there":
                if input("an idiot: ") == "an idiot who":
                    print("you")
                else:
                    YouDidntReplyCorrectly("With an idiot who")
            else:
                raise YouDidntReplyCorrectly("With who is there")
        if not self.activation_function in dir(yannl.activations):
            raise(NoActivationFunction("no activation function called " + self.activation_function))
        self.neurons = []
        for _ in range(num_of_neurons):
            self.neurons.append(neuron(self.activation_function))
class hiddenLayer(layers):
    def __init__(self, layerparhms, num_of_neurons, activation_function):
        super().__init__(layerparhms)
        self.purpose = "hidden"
        self.num_of_neurons = num_of_neurons
        self.activation_function = activation_function

class outputLayer(layers):
    def __init__(self, num_of_neurons, activation_function, layerparhms={}):
        super().__init__(layerparhms)
        self.purpose = "output"
        self.num_of_neurons = num_of_neurons
        self.activation_function = activation_function

    def make_neurons(self):
        time = 0
        for i in self.layerparhms:
            self.i = i["neuron" + time]
            time += 1
            print(self.i)

class neuron:
    '''
    Attributes
    ----------
    activation_function : str
        specify the name of the activation function 
        slope|sigmoid|relu|leaky_relu|parametric_relu|tanh|softmax|swish|step
    previous_to_current_weights : dict, optional
        specify the values of the weights from the previous layer to the current layer. set to "" for easier use in input layers
    current_to_next_weights : dict, optional
        specify the values of the weights from the next layer to the current one. set to "" for easier use in output layers.
    '''
    
    def __init__(self, activation_function, previous_to_current_weights="", current_to_next_weights=""): 
        self.activation_function = activation_function.strip()
        self.previous_to_current_weights = previous_to_current_weights
        self.current_to_next_weights = current_to_next_weights
    def activation(self,x) -> float:
        if self.activation_function in dir(yannl.activations):
            return eval("yannl.activations.%s(%s)" % (self.activation_function, x))
        if self.activation_function.strip() == "shit":
            raise(NoActivationFunction("shit is found"))
        raise(NoActivationFunction("no activation function called " + self.activation_function))

layer = inputLayer({"ws":{},"b":1}, 10, "swish")
for i in layer.neurons:
    print(i.__dict__)