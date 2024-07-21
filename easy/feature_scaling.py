import numpy as np
from typing import Tuple
def feature_scaling(data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # Your code here
    standardized_data = np.around((data - np.mean(data, axis=0)) / np.std(data, axis=0), 4)
    normalized_data = np.around((data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0)), 4)
    return standardized_data, normalized_data

if __name__=="__main__":
    data = np.array([[1, 2], [3, 4], [5, 6]])
    output = feature_scaling(data=data)
    print(output)