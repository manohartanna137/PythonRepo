import numpy as np
def find_max_min(row, column):
    array = []
    for i in range(row):
        array.append(list(map(int, input().split())))

    min_axis_one = np.min(array, axis=1)

    return np.max(min_axis_one)