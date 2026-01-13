import math

def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
            
    return True

# Ejemplo de uso
numero = 97
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
