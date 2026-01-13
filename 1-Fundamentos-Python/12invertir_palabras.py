frase = str(input("Introduce una frase: "))

frase_invertida = ""
for palabra in frase.split():
    frase_invertida = palabra + " " + frase_invertida

print(frase_invertida)