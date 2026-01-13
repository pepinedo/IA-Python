texto = str(input("Escribe una frase: "))

a = 0
e = 0
i = 0
o = 0
u = 0

for char in texto:
    if char == "a" or char == "A":
        a = a+1
    if char == "e" or char == "E":
        e = e+1
    if char == "i" or char == "I":
        i = i+1
    if char == "o" or char == "O":
        o = o+1
    if char == "u" or char == "U":
        u = u+1

print(f"Hay {a} a")
print(f"Hay {e} e")
print(f"Hay {i} i")
print(f"Hay {o} o")
print(f"Hay {u} u")