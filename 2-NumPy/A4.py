import numpy as np

x = np.array([12, -4, 7, 0, -9, 15, 3])

mask_neg  = x < 0

#Imprimir la máscara
print(mask_neg)

#Imprimir los valores negativos
print(x[mask_neg])

#Imprimir cuantos valores negativos hay
print(len(x[mask_neg]))

#Imprimir el porcentaje de negativos
print(100 / len(x) * len(x[mask_neg]), "%")

