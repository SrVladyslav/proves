# This notebook was created by Alex Aklson <<<<<<< 

import numpy as np 



def initialize_network(num_inputs, num_hidden_layers, num_nodes_hidden, num_nodes_output):
    
    num_nodes_previous = num_inputs # number of nodes in the previous layer

    network = {}
    
    # loop through each layer and randomly initialize the weights and biases associated with each layer
    for layer in range(num_hidden_layers + 1):
        
        if layer == num_hidden_layers:
            layer_name = 'output' # name last layer in the network output
            num_nodes = num_nodes_output
        else:
            layer_name = 'layer_{}'.format(layer + 1) # otherwise give the layer a number
            num_nodes = num_nodes_hidden[layer] 
        
        # initialize weights and bias for each node
        network[layer_name] = {}
        for node in range(num_nodes):
            node_name = 'node_{}'.format(node+1)
            network[layer_name][node_name] = {
                'weights': np.around(np.random.uniform(size=num_nodes_previous), decimals=2),
                'bias': np.around(np.random.uniform(size=1), decimals=2),
            }
    
        num_nodes_previous = num_nodes

    return network # return the network
'''
Use the initialize_network function to create a network that:
takes 5 inputs
has three hidden layers
has 3 nodes in the first layer, 2 nodes in the second layer, and 3 nodes in the third layer
has 1 node in the output layer
'''
### type your answer here
small_network = initialize_network(5, 3, [3,2,3], 1)

'''
The weighted sum at each node is computed as the dot product of the inputs and
the weights plus the bias. So let's create a function called compute_weighted_sum that does just that
'''
def compute_weighted_sum(inputs, weights, bias):
    return np.sum(inputs * weights) + bias

#	Let's generate 5 inputs that we can feed to small_network.
from random import seed
import numpy as np

np.random.seed(12)
inputs = np.around(np.random.uniform(size=5), decimals=2)
print('The inputs to the network are {}'.format(inputs))

#  Use the compute_weighted_sum function to compute the weighted sum at the first node in the first hidden layer
### type your answer here
node_weights = small_network['layer_1']['node_1']['weights']
node_bias = small_network['layer_1']['node_1']['bias']

weighted_sum = compute_weighted_sum(inputs, node_weights, node_bias)
print('The weighted sum at the first node in the hidden layer is {}'.format(np.around(weighted_sum[0], decimals=4)))

'''
Recall that the output of each node is simply a non-linear tranformation of the weighted sum. We use activation 
functions for this mapping. Let's use the sigmoid function as the activation function here. So let's define a 
function that takes a weighted sum as input and returns the non-linear transformation of the input using the sigmoid function.
'''
def node_activation(weighted_sum):
    return 1.0 / (1.0 + np.exp(-1 * weighted_sum))

# Use the node_activation function to compute the output of the first node in the first hidden layer.
node_output  = node_activation(compute_weighted_sum(inputs, node_weights, node_bias))
print('The output of the first node in the hidden layer is {}'.format(np.around(node_output[0], decimals=4)))

'''
Forward Propagation
The final piece of building a neural network that can perform predictions is to put everything together. 
So let's create a function that applies the compute_weighted_sum and node_activation functions to each node 
in the network and propagates the data all the way to the output layer and outputs a prediction for each node in the output layer.

The way we are going to accomplish this is through the following procedure:

Start with the input layer as the input to the first hidden layer.
Compute the weighted sum at the nodes of the current layer.
Compute the output of the nodes of the current layer.
Set the output of the current layer to be the input to the next layer.
Move to the next layer in the network.
Repeat steps 2 - 4 until we compute the output of the output layer.
'''
def forward_propagate(network, inputs):
    
    layer_inputs = list(inputs) # start with the input layer as the input to the first hidden layer
    
    for layer in network:
        
        layer_data = network[layer]
        
        layer_outputs = [] 
        for layer_node in layer_data:
        
            node_data = layer_data[layer_node]
        
            # compute the weighted sum and the output of each node at the same time 
            node_output = node_activation(compute_weighted_sum(layer_inputs, node_data['weights'], node_data['bias']))
            layer_outputs.append(np.around(node_output[0], decimals=4))
            
        if layer != 'output':
            print('The outputs of the nodes in hidden layer number {} is {}'.format(layer.split('_')[1], layer_outputs))
    
        layer_inputs = layer_outputs # set the output of this layer to be the input to next layer

    network_predictions = layer_outputs
    return network_predictions

# Use the forward_propagate function to compute the prediction of our small network_predictions
### type your answser here
pred = forward_propagate(small_network, inputs)
print('The predicted value is {}'.format(np.around(pred[0], decimals=4)))

'''
So we built the code to define a neural network. We can specify the number of inputs that a neural network can take, 
the number of hidden layers as well as the number of nodes in each hidden layer, and the number of nodes in the output layer.

We first use the initialize_network to create our neural network and define its weights and biases.
'''
my_network = initialize_network(5, 3, [2, 3, 2], 3)

# Then, for a given input,
inputs = np.around(np.random.uniform(size=5), decimals=2)

# We compute the network predictions.
predictions = forward_propagate(my_network, inputs)
print('The predicted values by the network for the given input are {}'.format(predictions))

### create a network
my_network = initialize_network(5, 4, [10, 32, 5,2], 3)
inputs = np.around(np.random.uniform(size=5), decimals=2)

predictions = forward_propagate(my_network, inputs)
print('The predicted values by the network for the given input are {}'.format(predictions))