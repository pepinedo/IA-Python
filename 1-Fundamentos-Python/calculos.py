import math

def area_circulo(radio):
    if radio < 0:
        return "El radio no puede ser negativo"
    return math.pi * (radio ** 2)