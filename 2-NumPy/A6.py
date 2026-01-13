import numpy as np

A = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
offset = np.array([1, 2, 3])

print("Shape de A: ", A.shape)
print("Shape de offset: ", offset.shape)
print("Resultado: \n", A + offset)

# ¿Porqué funciona? Porque numpy encuentra coincidencia en uno de los ejes.