diccionario = {"nombre": "Ana", "edad": 25}
# Acceso y actualización
diccionario.get("nombre") # "Ana"
diccionario.get("ciudad", "No disponible") # "No disponible"
diccionario.update({"ciudad": "Madrid"})
# Añadir y eliminar elementos
edad = diccionario.pop("edad") # edad = 25
diccionario.popitem() # Elimina ("ciudad", "Madrid") (el último para clave-valor agregado)
diccionario.clear() # {}
diccionario = {"nombre": "Ana", "edad": 25}
# Obtener claves, valores y elementos
claves = diccionario.keys() # dict_keys(['nombre', 'edad'])
valores = diccionario.values() # dict_values(['Ana', 25])
elementos = diccionario.items() # dict_items([('nombre', 'Ana'), ('edad', 25)])
# Copiar diccionarios
nuevo_diccionario = diccionario.copy()
##### RECORRIENDO DICCIONARIOS #####
datos = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
# Recorriendo claves
for clave in datos:
    print(clave)
# Recorriendo valores
for valor in datos.values():
    print(valor)
# Recorrer claves y valores
for clave, valor in datos.items():
    print(f"{clave}: {valor}")