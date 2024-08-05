import numpy as np

# Given points
points = np.array([(0, 0), (1, 2), (3, 4), (5, 6), (7, 8), (9, 10),
                  (11, 9), (12, 8), (13, 7), (14, 6), (15, 5), (16, 4), (17, 3), (18, 2), (19, 1), (20, 0)])

# Extracting x and y coordinates
x = points[:, 0]
y = points[:, 1]

# Calculating the necessary summations
n = len(points)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x_squared = np.sum(x ** 2)

# Calculating the coefficients a and b
a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b = (sum_y * sum_x_squared - sum_x * sum_xy) / (n * sum_x_squared - sum_x ** 2)

# Predicting y for x = 10
x_new = 15
y_new = a * x_new + b

# Printing the results
print(f"Regression model: y = {a:.2f}x + {b:.2f}")
print(f"Predicted value for x = {15}: y = {y_new:.2f}")
