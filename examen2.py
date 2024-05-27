def cuadrado():
    lado = float(input(f"Ingrese el valor del lado del cuadrado: "))
    area = lado * lado
    print(f"El área de un cuadrado de lado {lado} = {area}")

def triangulo():
    base = float(input(f"Ingrese el valor de la base del triángulo: "))
    altura = float(input(f"Ingrese el valor de la altura del triángulo: "))
    area = (base * altura)/2
    print(f"El área del triángulo = {area}")

def rectangulo():
    base = float(input(f"Ingrese el valor de la base del rectángulo: "))
    altura = float(input(f"Ingrese el valor de la altura del rectángulo: "))
    area = base * altura
    print(f"El área de un rectángulo de base {base} y altura {altura} = {area}")

while True:
    Calcular = input(f"Ingresa 1 para calcular el área de un cuadrado, 2 para un triángulo, 3 para un rectángulo y 's' para salir: ")
    if Calcular == "1":
        cuadrado()
    elif Calcular == "2":
        triangulo()
    elif Calcular == "3":
        rectangulo()
    elif Calcular == "s":
        break