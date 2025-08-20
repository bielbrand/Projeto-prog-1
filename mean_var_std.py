import numpy as np

def calculate(numbers):
    # Check input length
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list into 3x3 numpy array
    matrix = np.array(numbers).reshape(3, 3)

    # Build dictionary
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),   # column means
            matrix.mean(axis=1).tolist(),   # row means
            matrix.mean().item()            # overall mean
        ],
        'variance': [
            matrix.var(axis=0).tolist(),    # column variance
            matrix.var(axis=1).tolist(),    # row variance
            matrix.var().item()             # overall variance
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),    # column std
            matrix.std(axis=1).tolist(),    # row std
            matrix.std().item()             # overall std
        ],
        'max': [
            matrix.max(axis=0).tolist(),    # column max
            matrix.max(axis=1).tolist(),    # row max
            matrix.max().item()             # overall max
        ],
        'min': [
            matrix.min(axis=0).tolist(),    # column min
            matrix.min(axis=1).tolist(),    # row min
            matrix.min().item()             # overall min
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),    # column sum
            matrix.sum(axis=1).tolist(),    # row sum
            matrix.sum().item()             # overall sum
        ]
    }

    return calculations
