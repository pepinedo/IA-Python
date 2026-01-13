def factorial(n):
    if n == 0 or n == 1:
        print(1)
        return 1
    else:
        print(n-1)
        return n * factorial(n-1)
    
factorial(4)