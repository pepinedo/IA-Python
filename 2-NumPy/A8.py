import numpy as np

M = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

#Restar media a cada fila (resultado que no queremos, éste resta las medias de las filas a las columnas)
print(M - M.mean(axis=1))

#Restar media a cada fila (resultado que queremos)
print(M - M.mean(axis=1).reshape(-1,1))

#Es importante usar el reshape porque si no las restas no se hacen en el axis que quieres, si no el que coincide, siendo incorrecto. 