class layer:
    """
    layerparhms be like: {"weights":{"w1":w1, "w2":w2...}, "bias":bias} you can change "bias" to just "b" and "weights" to "ws".
    """
    def __init__(self, layerparhms: dict):
        self.layerparhms = layerparhms
        self.weights = self.findws()
        self.bias = self.findbias()
    def findbias(self):
        for i in self.layerparhms:
            if i == "b": return self.layerparhms["b"]
            if i == "bias": return self.layerparhms["bias"]
        raise errors.nobiaserr("no bias given in " + str(self.layerparhms))
    def findws(self):
        for i in self.layerparhms:
            if i == "ws": return self.layerparhms["ws"]
            if i == "weights": return self.layerparhms["weights"]
        raise errors.noweightserr("no weights were given in " + str(self.layerparhms))
    def backpropagation(self):
        pass