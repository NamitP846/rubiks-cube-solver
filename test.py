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

lista = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

x = np.where(a == 4)
i, j, k = int(x[0].item()), int(x[1].item()), int(x[2].item())
print(lista[i][j][k])