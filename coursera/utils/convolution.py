import numpy as np

def dimensions(image: np.ndarray, kernel: np.ndarray, padding:int, strides:int) -> np.ndarray:
    """
    See https://medium.com/analytics-vidhya/2d-convolution-using-python-numpy-43442ff5f381
    :param image:
    :param kernel:
    :param padding:
    :param strides:
    :return:
    """
    x_kern_shape = kernel.shape[0]
    y_kern_shape = kernel.shape[1]
    x_img_shape = image.shape[0]
    y_img_shape = image.shape[1]

    x_output = int(((x_img_shape - x_kern_shape + 2 * padding) / strides) + 1)
    y_output = int(((y_img_shape - y_kern_shape + 2 * padding) / strides) + 1)

    return np.zeros((x_output, y_output))


if __name__ == "__main__":

    dimensions(np.zeros(()), np.zeros(()), padding=1, strides=1)