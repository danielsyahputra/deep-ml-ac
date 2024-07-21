import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, 
                                       y: np.ndarray, 
                                       alpha: float, 
                                       iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(iterations):
        y_hat = np.dot(X, theta)
        error = y_hat - y.reshape(-1, 1)
        dw = (1 / m) * np.dot(X.T, error)
        theta -= alpha * dw
    return np.around(theta, 4)

if __name__=="__main__":
    X = np.array([[1, 1], [1, 2], [1, 3]]) 
    y = np.array([1, 2, 3])
    alpha = 0.01
    iterations = 1000
    output = linear_regression_gradient_descent(X, y, alpha, iterations)
    print(output)