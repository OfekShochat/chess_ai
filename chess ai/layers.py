from errors import *

class layer:
    """
    layerparhms be like: {"weights":{"w1":w1, "w2":w2...}, "bias":bias} you can change "bias" to just "b" and "weights" to "ws".
    """
    def __init__(self, layerparhms: dict, purpose: str):
        self.layerparhms = layerparhms
        self.weights = self.findws()
        self.bias = self.findbias()
        self.purpose = purpose
    def findbias(self):
        for i in self.layerparhms:
            if i == "b": return self.layerparhms["b"]
            if i == "bias": return self.layerparhms["bias"]
        raise nobiaserr("no bias given in " + str(self.layerparhms))
    def findws(self):
        for i in self.layerparhms:
            if i == "ws": return self.layerparhms["ws"]
            if i == "weights": return self.layerparhms["weights"]
        raise noweightserr("no weights were given in " + str(self.layerparhms))
    def backpropagation(self):
        pass