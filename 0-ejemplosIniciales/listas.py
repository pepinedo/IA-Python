lista = [1, 2, 3]
# Adición de elementos
lista.append(4) # [1, 2, 3, 4]
lista.extend([5, 6]) # [1, 2, 3, 4, 5, 6]
lista.insert(1, 99) # [1, 99, 2, 3, 4, 5, 6]
# Eliminación de elementos
lista.remove(99) # [1, 2, 3, 4, 5, 6]
eliminado = lista.pop(2) # eliminado = 3, lista = [1, 2, 4, 5, 6]
lista.clear() # []
numeros = [3, 1, 4, 2]
# Ordenación y búsqueda
numeros.sort() # [1, 2, 3, 4]
nueva_lista = sorted(numeros, reverse=True) # [4, 3, 2, 1]
posicion = numeros.index(3) # 2
repeticiones = numeros.count(3) # 1
# Otras operaciones
numeros.reverse() # [4, 3, 2, 1]
copia = numeros.copy()

##### RECORRIENDO LISTAS #####
numeros = [10, 20, 30, 40]
# for
for num in numeros:
    print(num)
# for ... enumerate
for i, num in enumerate(numeros):
    print(f"Índice {i}: {num}")
# while (hay que calcular la longitud para tener una condición de parada)
while i < len(numeros):
    print(numeros[i])
    i += 1