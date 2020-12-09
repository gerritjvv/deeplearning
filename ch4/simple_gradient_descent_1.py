
def run():
    input = 0.5
    goal = 0.8
    alpha = 0.01
    weight = 0.5

    for i in range(20000):
        pred = weight * input
        error = (pred - goal) ** 2  # squared error

        if error < 9.603747960254256e-20:
            break

        weight_delta = (pred - goal) * input

        print(f"[{i}] Error {error} w_delta {weight_delta} pred {pred} weight {weight}")

        weight -= weight_delta * alpha

    print(f"weight {weight} pred {pred}")


if __name__ == "__main__":
    run()
