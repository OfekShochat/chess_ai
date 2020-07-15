class net:
    def __init__(self, inputs: dict):
        self.inputs = inputs
    
    def bind(self, *layers):
        for layer in layers:
            print(layer.weights)