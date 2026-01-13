# Conversion de tipos
x = 10
y = 20.5
z = "30"
suma = x + y + int(z) # Convertir z a entero
print(f"La suma es: {suma}") # La suma es: 60.5
# Manipulación de cadenas
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido # Concatenación
print(f"Nombre completo: {nombre_completo}") # Nombre completo: Juan Pérez
edad = 25

mensaje = f"Hola, me llamo {nombre} {apellido} y tengo {edad} años." # F-strings

print(mensaje) # Hola, me llamo Juan Pérez y tengo 25 años.
texto = " Hola, ¿cómo estás? "
print(texto.upper()) # Convertir a mayúsculas → " HOLA, ¿CÓMO ESTÁS?"
print(texto.strip()) # Eliminar espacios en blanco → "Hola, ¿cómo estás?"
print(texto.replace("estás", "te encuentras")) # Reemplazar texto → " Hola, ¿cómo te encuentras? "