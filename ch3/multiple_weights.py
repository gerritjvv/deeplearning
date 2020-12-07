weights = [0.5, 1, -1]

inputs = [0.4, 0.2, 3]


def weighted_sum(weights, input):
    sum = 0
    for w in weights:
        sum += (w * input)

    return sum


def predict(weights, input):
    return weighted_sum(weights, input)


for input in inputs:
    print(predict(weights, input))


# 0.5
# 0.1
# 1.5