import numpy as np


# Define the ReLU activation function for scalar inputs
#
def relu(x):
    return np.maximum(0, x)


# Function to compute the output of a single neuron network
#
# inputs: vector
# weights: vector
# bias: scalar
#
def single_neuron_network(weights, bias, inputs):

    # Calculate the neuron's output before activation
    output_before_activation = sum(w * i for w, i in zip(weights, inputs)) + bias

    # Apply the ReLU activation function
    activated_output = relu(output_before_activation)


    return output_before_activation, activated_output


# Given values for single node network
#
inputs = np.array([2, 1, 3])
weights = np.array([1, -1, 1])
bias = -5  # bias should be a scalar, not an array

# Perform the operation
#
output_before_activation, activated_output = single_neuron_network(weights, bias, inputs)

print("\n")

print("output_before_activation: ", output_before_activation)
print("\n")
print("activated_output: ", activated_output)
print("\n")
