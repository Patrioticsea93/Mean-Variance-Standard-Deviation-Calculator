import numpy as np

def calculator(operator, matrix):
    if operator == "sum":
        axis1 = matrix.sum(axis=0).tolist()
        axis2 = matrix.sum(axis=1).tolist()
        flattened = matrix.sum()
    elif operator == "min":
        axis1 = matrix.min(axis=0).tolist()
        axis2 = matrix.min(axis=1).tolist()
        flattened = matrix.min()
    elif operator == "max":
        axis1 = matrix.max(axis=0).tolist()
        axis2 = matrix.max(axis=1).tolist()
        flattened = matrix.max()
    elif operator == "std":
        axis1 = matrix.std(axis=0).tolist()
        axis2 = matrix.std(axis=1).tolist()
        flattened = matrix.std()
    elif operator == "var":
        axis1 = matrix.var(axis=0).tolist()
        axis2 = matrix.var(axis=1).tolist()
        flattened = matrix.var()
    elif operator == "mean":
        axis1 = matrix.mean(axis=0).tolist()
        axis2 = matrix.mean(axis=1).tolist()
        flattened = matrix.mean()
    return [axis1, axis2, flattened]

def calculate(mylist):
    if len(mylist) != 9:
        raise ValueError("The List must contain nine numbers for this to work.")
  
    else:
        matrix = np.array(mylist).reshape(3, 3)
        calculations = {
                        'mean': calculator('mean', matrix),
                        'variance': calculator('var', matrix),
                        'standard deviation': calculator('std', matrix),
                        'max': calculator('max', matrix),
                        'min': calculator('min', matrix),
                        'sum': calculator('sum', matrix),
                        }

    return calculations
