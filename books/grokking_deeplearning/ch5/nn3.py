import numpy as np

np.random.seed(1)


def relu(x):
    if x > 0:
        return x
    return 0


alpha = 0.2
hidden_size = 4

streetlights = np.array([[1, 0, 1],
                         [0, 1, 1],
                         [0, 0, 1],
                         [1, 1, 1]])

walk_vs_stop = np.array([[ 1, 1, 0, 0]]).T

weights_0_1 = np.random.random((3, hidden_size)) - 1
weights_1_2 = np.random.random((hidden_size, 1)) - 1

layer_0 = streetlights[0]
layer_1 = relu(layer_0.dot(weights_0_1))
layer_2 = layer_1.dot(weights_1_2)
