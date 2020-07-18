class net:
    def __init__(self, *layers):
        self.layers = layers
    
    def bind(self):
        for layer in self.layers:
            print(layer.weights)