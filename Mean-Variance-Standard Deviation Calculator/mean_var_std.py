import numpy as np


def calculate(list):
    if len(list) == 9:
        one_d = np.array(list)
        np_array = one_d.reshape(3, 3)

        calculations = {
            'mean': [np.mean(np_array, axis=0).tolist(), np.mean(np_array, axis=1).tolist(), np.mean(np_array.flatten())],
            'variance': [np.var(np_array, axis=0).tolist(), np.var(np_array, axis=1).tolist(), np.var(np_array.flatten())],
            'standard deviation': [np.std(np_array, axis=0).tolist(), np.std(np_array, axis=1).tolist(), np.std(np_array.flatten())],
            'max': [np.max(np_array, axis=0).tolist(), np.max(np_array, axis=1).tolist(), np.max(np_array.flatten())],
            'min': [np.min(np_array, axis=0).tolist(), np.min(np_array, axis=1).tolist(), np.min(np_array.flatten())],
            'sum': [np.sum(np_array, axis=0).tolist(), np.sum(np_array, axis=1).tolist(), np.sum(np_array.flatten())]
        }
        return calculations

    else:
        raise ValueError("List must contain nine numbers.")
