#
# Learning is just reducing error. You can modify the weight to reduce the error.
#
import random

def run():
    input = 0.5
    goal = 0.8
    alpha = 0.01
    weight = random.random()

    for i in range(20000):
        pred = weight * input

        error = (pred - goal) ** 2  # squared error

        if error < 9.603747960254256e-20:
            break

        # calculations direction and amount from error
        # contains pure error (pred - goal). Multiplying by the input provides scaling, negative reversal and stopping.
        #  stopping: if input is zero the the update is zero also
        #  negative reversal:  When input is negative, moving the weight up makes the prediction go down, its reversed.
        #                       Multiplying by the negative input reverses the sign again. This ensures the weight
        #                       moves in the correct direction.
        #  scaling: Big pure errors are amplified while smaller errors are nearly ignored.
        #
        direction_and_amount = (pred - goal) * input

        print(f"[{i}] Error {error} w_delta {direction_and_amount} pred {pred} weight {weight}")

        weight -= direction_and_amount * alpha

    print(f"weight {weight} pred {pred}")


if __name__ == "__main__":
    run()
