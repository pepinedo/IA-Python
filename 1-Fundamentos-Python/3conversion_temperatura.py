temperatura_c = 25
temperatura_f = 32

def convertir_temperatura(temperatura, grados):
    if grados == "f":
        x = temperatura * 1.8
        x + 32
    elif grados == "c":
        x = temperatura - 32
        x / 1.8
    return x

print(convertir_temperatura(temperatura_c, "f"))
print(convertir_temperatura(temperatura_f, "c"))