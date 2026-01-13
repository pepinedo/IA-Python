try:
    with open("datos.txt", 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        total = len(lineas)
        print(f"El archivo '{archivo.name}' tiene {total} líneas.")
except FileNotFoundError:
    print(f"Error: El archivo '{archivo.name}' no existe.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")