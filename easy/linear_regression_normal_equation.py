import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)
    return np.around(np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y), 4).flatten().tolist()