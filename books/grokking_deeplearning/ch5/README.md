Prediction is the weighted sum of the inputs. The learning algorithm rewards inputs that correlate with the output with
upward pressure toward 1 on their weight, while penalizing inputs with discorrelation with downward pressure.

The weighted sumt of the inputs find perfect correlation between the input and the output by weighting decorrelated
inputs to 0.

e.g weights in nn2.py are ```[ 0.01389228  1.0138147  -0.01599277]``` , the middle weight
is ~1 which means it correlated better to the output that the left and right weights.

If you train the network on only the first 2 examples, it would "overfit" by just memorizing
the examples intead of learning the general weigths that can be used for other unkown examples.

The greated challenge for AI is have the network generalize instead of memorize.


Edge case:

Inputs with both upward and downward pressure. Regularisation is used to set the weights for these inputs
to zero. These kind of inputs do not help with prediction.


Indirection:

If your data does not have correlation, create intermediate data that does.

Backpropagation:

n the neural network from chapter 5, the delta variable told you the direction and amount the value of this node should change next time. 
All backpropagation lets you do is say, “Hey, if you want this node to be x amount higher, 
then each of these previous four nodes needs to be x*weights_1_2 amount higher/lower, because these weights were amplifying the prediction by weights_1_2 times.” 

For each weight multiply its input by its output delta and increase the weight value by it.
