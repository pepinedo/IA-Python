def filtrar_pares(lista):
    nuevaLista = []

    for numero in lista:
        if numero % 2 == 0:
            nuevaLista.append(numero)

    print(nuevaLista)
    return nuevaLista

filtrar_pares([1,2,3,4,5])