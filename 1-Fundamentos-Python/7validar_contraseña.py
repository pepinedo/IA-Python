password = str(input("Escriba su contraseña: "))

def validar_contraseña(password):
    if len(password) < 8:
        return print("❌ La contraseña debe de tener 8 caracteres o más ❌")
    if (not any(char.isupper() for char in password)):
        return print("❌ La contraseña debe de tener, al menos, una mayúscula ❌")
    if (not any(char.islower() for char in password)):
        return print("❌ La contraseña debe de tener, al menos, una minúscula ❌")
    if (not any(char.isnumeric() for char in password)):
        return print("❌ La contraseña debe de tener, al menos, un número ❌")
    print("✅ Contraseña aceptada ✅")
    
validar_contraseña(password)