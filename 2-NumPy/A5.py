import numpy as np

x = np.array([12, -4, 7, 0, -9, 15, 3])

#Copia del array
x_copy = x.copy()

#Máscara que identifica los negativos
mask = x < 0

#El nuevo array con los negativos cambiados por 0
x_copy[mask] = 0

print(x)
print(x_copy)

