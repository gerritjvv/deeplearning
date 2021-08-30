
import numpy as np

weights = np.array([0.5, 0.0, -0.7])
alpha = 0.1

streetlights = np.array( [ [ 1, 0, 1 ],
                            [ 0, 1, 1 ],
                            [ 0, 0, 1 ],
                            [ 1, 1, 1 ],
                            [ 0, 1, 1 ],
                            [ 1, 0, 1 ] ] )

walk_vs_stop = np.array([0,1,0,1,1,0])


for i in range(len(streetlights)):
    i = 0
    input = streetlights[i]
    goal_prediction = walk_vs_stop[i]

    for iteration in range(1):
        prediction = input.dot(weights)
        error = (prediction - goal_prediction) ** 2
        if error > 0.00010955709799813623:
            delta = prediction - goal_prediction

            weights = weights - (alpha * (input * weights))

            print(f"Error {error}. Prediction: {prediction}")

