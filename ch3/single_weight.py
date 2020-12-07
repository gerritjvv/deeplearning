weight = 0.5

inputs = [1, 0.2, 3]


def weighted_sum(weight, input):
    return weight * input


def predict(weight, input):
    return weighted_sum(weight, input)


for input in inputs:
    print(predict(weight, input))
