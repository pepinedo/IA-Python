tupla = (1, 2, 3, 2, 2)
# Operaciones básicas
tupla.count(2) # 3
tupla.index(3) # 2
# Conversión a lista, añadir un elemento y reconvertir a tupla
lista = list(tupla)
lista.append(4)
tupla = tuple(lista)
##### SE RECORREN IGUAL QUE LAS LISTAS #####