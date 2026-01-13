def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        print(n)
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
numero = int(input("Ingresa un número: "))
fibonacci_recursivo(numero)