import numpy as np

from src.config import COST_MATRIX

def evaluate_cost(y_true, y_pred):
    cost = COST_MATRIX[y_true, y_pred]
    return cost.sum(), cost


if __name__ == "__main__":
    evaluate_cost(np.array([0, 0, 4]), np.array([1, 0, 0]))