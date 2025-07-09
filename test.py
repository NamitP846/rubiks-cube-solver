import numpy as np

a = np.array([
    top:=[
        [1, 2],
        [3, 4],
    ],bottom:=[
        [5, 6],
        [7, 8]
    ]
])

a = np.rot90(a, k=1, axes=(0, 1))
print(a)