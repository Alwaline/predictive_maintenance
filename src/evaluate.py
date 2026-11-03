import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

from src.config import COST_MATRIX
from src.data import load_flattened_data
from src.modeling import build_train_table, build_eval_table


def evaluate_cost(y_true, y_pred):
    cost = COST_MATRIX[y_true, y_pred]
    return cost.sum(), cost


def evaluate_metrics(y_true, y_pred, print_metrics=True):
    cost, _ = evaluate_cost(y_true, y_pred[:, 0])
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    confusion = confusion_matrix(y_true, y_pred)
    if print_metrics:
        print("Predictive cost:", cost)
        print("Classification report:\n", classification_report(y_true, y_pred, zero_division=0))
        print("Confusion matrix:\n", confusion_matrix(y_true, y_pred))
    return cost, report, confusion


def evaluate_catboost(model, X, y_true, print_metrics=False):
    y_pred = model.predict(X)
    return evaluate_metrics(y_true, y_pred, print_metrics=print_metrics)


def eval_n_class(class_lable: int, print_metrics=False):
    df_val = load_flattened_data("validation")
    _, y_val, _ = build_eval_table(df_val)
    cost, report, confusion_matrix = evaluate_metrics(y_val, np.full(y_val.shape, class_lable).reshape(-1, 1), print_metrics=print_metrics)
    return cost, report, confusion_matrix


if __name__ == "__main__":
    evaluate_cost(np.array([0, 0, 4]), np.array([1, 0, 0]))