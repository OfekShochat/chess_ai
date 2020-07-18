import numpy as np
from scipy.stats import linregress

def slope(x, alpha=0.1):
    return x * (1-x) * alpha
print(slope(10, 0.1))

def sigmoid(x):
    return 1/(1+np.exp(-x))

#relu functions:
def relu(x):
    return max(0, x)
def leaky_relu(x):
    return np.where(x > 0, x, x * 0.01)
def parametric_relu(x, a=2):
    max(a * x, x)


def tanh(x):
    np.tanh(x)

def softmax(x):
    expo = np.exp(x)
    expo_sum = np.sum(np.exp(x))
    return expo/expo_sum

def swish(x):
    return x * sigmoid(x)