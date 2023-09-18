#sigmoid activation function
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Example usage as an activation function
input_data = np.array([0.5, -1.0, 2.0])
weights = np.array([0.1, -0.2, 0.5])
bias = 0.2
z = np.dot(input_data, weights) + bias
activation = sigmoid(z)
print("Activation:", activation)


