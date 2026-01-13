import numpy as np

M = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

print("Suma total: ", M.sum())
print(M.sum().shape)
print("Suma por columnas: ", M.sum(axis=0))
print(M.sum(axis=0).shape)
print("Suma por filas: ", M.sum(axis=1))
print(M.sum(axis=1).shape)
print("Media por columnas: ", M.mean(axis=0))
print(M.mean(axis=0).shape)
print("Media por filas: ", M.mean(axis=1))
print(M.mean(axis=1).shape)

#La media que más sentido puede tener es la media de columnas, porque suelen ser los mismos tipos de datos, como, por ejemplo, el salario.