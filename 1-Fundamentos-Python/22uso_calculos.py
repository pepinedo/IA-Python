from calculos import area_circulo

try:
    radio = float(input("Introduce el radio del círculo: "))
    area = area_circulo(radio)
    print(f"{area:.4f}")
except ValueError:
    print(ValueError)

