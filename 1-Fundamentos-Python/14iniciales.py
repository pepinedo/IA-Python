nombre = str(input("Introduce tu nombre y apellidos: "))

iniciales = ""
for palabra in nombre.split():
    iniciales = iniciales + palabra[0].capitalize()

print(iniciales)