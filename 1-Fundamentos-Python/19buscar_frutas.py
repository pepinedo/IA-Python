frutas = ("manzana", "fresa", "uva", "naranja", "kiwi")

pregunta = str(input("Dime una fruta: "))
if pregunta in frutas:
    print(f"Si, tenemos {pregunta}")
else:
    print(f"No, no tenemos {pregunta}")