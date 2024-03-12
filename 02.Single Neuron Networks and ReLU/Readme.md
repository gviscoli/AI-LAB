# Single Neuron

## Activation functions
Activation functions play a crucial role in neural networks by introducing non-linearity into the model. They help determine the output of a neuron based on the weighted sum of its inputs and the bias term. Activation functions have various forms, and the choice of a particular function depends on the problem being solved and the desired properties of the network.

### Sigmoid Function
A continuous, S-shaped function that maps input values to a range between 0 and 1. It is useful for binary classification tasks and outputting probabilities.

### Hyperbolic Tangent (tanh) Function
Another continuous, S-shaped function that maps input values to a range between -1 and 1. It is often preferred over the sigmoid function in hidden layers due to its zero-centered output.

### ReLU Function
A piecewise linear function that outputs the input value if it is positive, and zero otherwise. ReLU has become popular due to its computational efficiency and ability to mitigate the vanishing gradient problem.

The ReLU(x) function embodies the ReLU (Rectified Linear Unit) activation function. It returns x if x is positive, and zero otherwise. 

This function is key for introducing non-linearity, enabling neural networks to tackle complex problems.



## Neuron Simulation

![AI is fun!](/Assets/Images/SingleNode.png "Single Node Neuron")

<b>Weights and Inputs</b>: Each input is multiplied by its corresponding weight. The weights are adjusted during training to refine the network’s accuracy

<b>Bias</b>: Adding the bias to the sum of weighted inputs provides an extra layer of flexibility, allowing the neuron to fine-tune its output.

<b>ReLU</b>: The output from the linear calculation is then fed through the ReLU function. This is where non-linearity comes into play, empowering the network with the ability to learn and model intricate patterns.