
## Notes:

Sigmoid: 
```
f(x) = 1/(1+e^-x)
```

Derivative:

```
s = sigmoid(x)
s*(1-s) 
```


Nomalisation: `softmax, when you need to classify N categories`

Image 2 Vector

```python
def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    v = np.reshape(image, (image.shape[0]*image.shape[1]*image.shape[2], 1))
    ### END CODE HERE ###
    
    return v
```

# To Remember

````
    np.exp(x) works for any np.array x and applies the exponential function to every coordinate
    the sigmoid function and its gradient
    image2vector is commonly used in deep learning
    np.reshape is widely used. In the future, you'll see that keeping your matrix/vector dimensions straight will go toward eliminating a lot of bugs.
    numpy has efficient built-in functions
    broadcasting is extremely useful
````

# Loss function:

```python
import numpy as np

def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    loss = np.sum(np.absolute(y - yhat), axis=0)
    ### END CODE HERE ###
    
    return loss


yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat,y)))
```

```python
# GRADED FUNCTION: L2
import numpy as np

def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    l1 = np.absolute(y - yhat)
    loss = np.sum(np.dot(l1, l1), axis=0)
    ### END CODE HERE ###
    
    return loss

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))
```


## To Remember 
```
    Vectorization is very important in deep learning. It provides computational efficiency and clarity.
    You have reviewed the L1 and L2 loss.
    You are familiar with many numpy functions such as np.sum, np.dot, np.multiply, np.maximum, etc...
```