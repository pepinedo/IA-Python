diccionario = {"España":"Madrid", "Francia":"París", "Italia":"Roma"}

pregunta = str(input("Introduce un país: "))

if pregunta in diccionario:
    print(f"La capital de {pregunta} es {diccionario.get(pregunta)}")